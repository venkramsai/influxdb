import requests
from random import randint
import time

DATA_SIZE = 144000000
LOCAL_URL = 'http://localhost:8086/write?db=perf_test_flows1'
OPENSTACK_URL = 'http://10.0.68.41:8086/write?db=perf_test_flows1'
BULK_INSERT_SIZE = 5000
NUM_SITES = 1001
NUM_ZONES_PER_SITE = 11
NUM_APPS = 997

ts_start = 1494055562000000
# ts_start = 1494006006000000


'''
SCHEMA 1:
    Measurement: flows_data
    Tagset: zone_id, site_id, app_id
    Fieldset: qos_id, wan_id, rule_id, in_pkts, out_pkts, in_bytes, out_bytes
'''


def generate_data_schema1(start_ts, end_ts):
    i = 0
    data_array = []
    for ts in xrange(start_ts, end_ts):
        data_string = 'flows_data'
        # generate tagset
        data_string += ',zone_id=' + str(i % (NUM_ZONES_PER_SITE * NUM_SITES))
        data_string += ',site_id=' + str(i % NUM_SITES)
        data_string += ',app_id=' + str(i % NUM_APPS)

        data_string += ' qos_id=' + str(randint(1, 4))
        data_string += ',wan_id=' + str(randint(0, 10))
        data_string += ',rule_id=' + str(randint(0, 50))
        data_string += ',in_pkts=' + str(randint(0, 10000))
        data_string += ',out_pkts=' + str(randint(0, 10000))
        data_string += ',in_bytes=' + str(randint(0, 100000))
        data_string += ',out_bytes=' + str(randint(0, 100000))
        data_string += ' ' + str(ts)
        i += 1
        data_array.append(data_string)
    return data_array


def post_to(url):
    total_time_writing = 0
    for i in xrange(DATA_SIZE / BULK_INSERT_SIZE):
        data_arr = generate_data_schema1(
            ts_start + (i * BULK_INSERT_SIZE), ts_start + ((i + 1) * BULK_INSERT_SIZE))
        print "Writing segment: " + str(i * BULK_INSERT_SIZE) + " to " + str((i + 1) * BULK_INSERT_SIZE)
        start = time.time()
        r = requests.post(url,
                          data='\n'.join(data_arr),
                          headers={'Content-Type': 'application/octet-stream'})
        end = time.time()
        total_time_writing += (end - start)
    print str(DATA_SIZE) + " records written in " + str(total_time_writing) + 's'
    return r

# post_to(OPENSTACK_URL)
post_to(LOCAL_URL)
