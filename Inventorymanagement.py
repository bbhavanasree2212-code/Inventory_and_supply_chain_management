# InventoryManagement.py

warehouses = {
    "A": {"Laptop": 10, "Mouse": 5},
    "B": {"Laptop": 3, "Keyboard": 8},
    "C": {"Laptop": 7, "Mouse": 2}
}

suppliers = {
    "Laptop": "ABC Suppliers",
    "Mouse": "XYZ Suppliers",
    "Keyboard": "PQR Suppliers"
}

LOW_STOCK = 3


# Add product
def add_product(warehouse, product, qty):
    warehouses[warehouse][product] = warehouses[warehouse].get(product, 0) + qty
    print(f"Added {qty} {product} to Warehouse {warehouse}")


# Remove product
def remove_product(warehouse, product, qty):
    if warehouses[warehouse].get(product, 0) >= qty:
        warehouses[warehouse][product] -= qty
        print(f"Removed {qty} {product} from Warehouse {warehouse}")
    else:
        print("Insufficient stock")


# Transfer stock
def transfer_stock(src, dest, product, qty):
    if warehouses[src].get(product, 0) >= qty:
        warehouses[src][product] -= qty
        warehouses[dest][product] = warehouses[dest].get(product, 0) + qty
        print(f"Transferred {qty} {product} from {src} to {dest}")
    else:
        print("Transfer failed: Insufficient stock")


# Reorder
def reorder(warehouse, product, qty):
    add_product(warehouse, product, qty)
    print(f"Reordered {qty} {product}")


# Supplier management
def supplier(product):
    print(f"Supplier for {product}: {suppliers.get(product, 'Not available')}")


# Low-stock detection
def low_stock():
    print("\nLow Stock:")
    for w, products in warehouses.items():
        for product, qty in products.items():
            if qty <= LOW_STOCK:
                print(f"Warehouse {w}: {product} = {qty}")


# Automatic warehouse selection
def select_warehouse(product, qty):
    for w in ["A", "B", "C"]:
        if warehouses[w].get(product, 0) >= qty:
            print(f"Order should be fulfilled from Warehouse {w}")
            return w

    print("No warehouse has enough stock")
    return None


# ---------------- MAIN ----------------

add_product("A", "Laptop", 5)
remove_product("B", "Laptop", 1)

transfer_stock("A", "C", "Mouse", 2)

reorder("B", "Keyboard", 5)

supplier("Laptop")

low_stock()

select_warehouse("Laptop", 5)
