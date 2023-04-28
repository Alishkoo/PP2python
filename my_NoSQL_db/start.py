from database import Database

a = Database("Firstdb")

a.create_table("example", ["ss"])
a.insert("example", {"id" : 1, "name" : "Alibek" , "age" : 18})
a.insert("example", {"id" : 2, "name" : "Alex" , "age" : 32})
a.insert("example", {"id" : 3, "name" : "Didar" , "age" : 48})

# all_records = a.select("example")

# filtered_records = a.select("example", condition=lambda row: row["age"] > 30)


# sorted_records = a.select("example", order_by={"column": "id", "reverse": True})

# a.update("example", {"id": 1}, {"age": 30})

a.delete("example", {"id": 1})

# print(all_records, filtered_records, sorted_records, a.select("example"))