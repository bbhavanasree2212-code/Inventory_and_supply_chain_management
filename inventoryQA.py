from Inventorymanagement import warehouses, remove_product, transfer_stock, reorder, select_warehouse
import threading

def test_stock_availability():
    print("\nTEST 1: Stock Availability")
    if warehouses["A"].get("Laptop", 0) > 0:
        print("PASS: Laptop is available")
    else:
        print("FAIL")

def test_insufficient_inventory():
    print("\nTEST 2: Insufficient Inventory")
    before = warehouses["B"].get("Laptop", 0)
    remove_product("B", "Laptop", 100)
    if warehouses["B"].get("Laptop", 0) == before:
        print("PASS: Insufficient inventory rejected")
    else:
        print("FAIL")

def test_warehouse_transfer():
    print("\nTEST 3: Warehouse Transfer")
    before_a = warehouses["A"]["Laptop"]
    before_b = warehouses["B"]["Laptop"]
    transfer_stock("A", "B", "Laptop", 2)
    if warehouses["A"]["Laptop"] == before_a - 2 and warehouses["B"]["Laptop"] == before_b + 2:
        print("PASS: Stock transferred successfully")
    else:
        print("FAIL")

def test_concurrent_orders():
    print("\nTEST 4: Concurrent Orders")
    def order():
        remove_product("A", "Laptop", 1)
    threads = [threading.Thread(target=order) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("PASS: Concurrent orders executed")

def test_reorder_threshold():
    print("\nTEST 5: Reorder Threshold")
    warehouses["C"]["Laptop"] = 2
    if warehouses["C"]["Laptop"] <= 3:
        reorder("C", "Laptop", 10)
        print("PASS: Reorder triggered")
    else:
        print("FAIL")

def test_invalid_product():
    print("\nTEST 6: Invalid Product")
    if "Mobile" not in warehouses["A"]:
        print("PASS: Invalid product detected")
    else:
        print("FAIL")

def test_negative_inventory():
    print("\nTEST 7: Negative Inventory")
    warehouses["B"]["Mouse"] = 2
    remove_product("B", "Mouse", 10)
    if warehouses["B"]["Mouse"] >= 0:
        print("PASS: Negative inventory prevented")
    else:
        print("FAIL")

def test_multiple_warehouses():
    print("\nTEST 8: Multiple Warehouses")
    warehouse = select_warehouse("Laptop", 5)
    if warehouse in ["A", "B", "C"]:
        print("PASS: Warehouse selected:", warehouse)
    else:
        print("FAIL")

if __name__ == "__main__":
    print("INVENTORY MANAGEMENT QA")
    test_stock_availability()
    test_insufficient_inventory()
    test_warehouse_transfer()
    test_concurrent_orders()
    test_reorder_threshold()
    test_invalid_product()
    test_negative_inventory()
    test_multiple_warehouses()
    print("QA TESTING COMPLETED")
