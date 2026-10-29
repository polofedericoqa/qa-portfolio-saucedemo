-- ====================================================================
-- QA DATABASE TESTING - SAUCEDEMO E-COMMERCE VERIFICATIONS
-- ====================================================================
-- Questo script contiene query SQL per validare l'integrità dei dati
-- sul database relazionale a seguito dei test eseguiti sul frontend.
-- Tools: TablePlus / DBNgin / PostgreSQL / MySQL
-- ====================================================================

-- --------------------------------------------------------------------
-- 1. VERIFICA UTENTI E STATO ACCOUNT
-- --------------------------------------------------------------------

-- TC-LOG-001: Verifica presenza dell'utente standard e stato attivo
SELECT user_id, username, email, is_active, created_at
FROM users
WHERE username = 'standard_user';

-- TC-LOG-002: Identificazione utenti bloccati nel sistema
SELECT user_id, username, is_active, lock_reason
FROM users
WHERE is_active = FALSE OR lock_reason IS NOT NULL;


-- --------------------------------------------------------------------
-- 2. VERIFICA CATALOGO PRODOTTI E GIACENZE DI MAGAZZINO
-- --------------------------------------------------------------------

-- TC-CRT-001: Verifica prezzo e disponibilità stock prima e dopo l'acquisto
SELECT product_id, product_name, price, stock_quantity
FROM products
WHERE product_name LIKE '%Backpack%' OR product_name LIKE '%Bike Light%';

-- Controllo prodotti fuori stock (Edge Case / BVA)
SELECT product_id, product_name, stock_quantity
FROM products
WHERE stock_quantity <= 0;


-- --------------------------------------------------------------------
-- 3. VERIFICA ORDINI E CHECKOUT (JOIN BETWEEN TABLES)
-- --------------------------------------------------------------------

-- TC-CHK-001: Controllo integrità dell'ultimo ordine creato dall'utente
SELECT 
    o.order_id,
    u.username,
    u.email,
    o.total_amount,
    o.shipping_zip_code,
    o.order_status,
    o.created_at
FROM orders o
JOIN users u ON o.user_id = u.user_id
WHERE u.username = 'standard_user'
ORDER BY o.created_at DESC
LIMIT 1;

-- Dettaglio articoli associati all'ordine appena effettuato
SELECT 
    oi.order_id,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS subtotal
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id = 1001;


-- --------------------------------------------------------------------
-- 4. INTEGRITÀ DEI DATI E AUDIT
-- --------------------------------------------------------------------

-- Controllo discrepanze sul totale dell'ordine (Backend vs Frontend)
SELECT 
    order_id,
    SUM(quantity * unit_price) AS calculated_total
FROM order_items
GROUP BY order_id
HAVING calculated_total <= 0;
