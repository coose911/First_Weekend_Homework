def get_name(record_store):
    return record_store["name"]

def find_record_by_title(title, record_store):
    list_of_records = record_store["records"]
    for record in list_of_records:
        if record["title"] == title:
            return record

def sell_record(record, record_store):
    cost_of_record = record["price"]
    record_store["money"] += cost_of_record
    list_of_records = record_store["records"]
    list_of_records.remove(record)
