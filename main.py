from adtrackQuery.query import adtrackQuery


print(adtrackQuery("SELECT * FROM at_call_log cl WHERE cl.parent_id='Ch4NI1f1OV86zQAb' LIMIT 10"))
