import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(user='postgres', password='1q2w3E4R', host='127.0.0.1')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cmd_revoke = f"REVOKE CONNECT ON DATABASE fast_api_db FROM public, postgres;"
cur.execute(cmd_revoke)
conn.commit()
cur.execute("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = "
            "'fast_api_db' AND pid <> pg_backend_pid();")
conn.commit()
cur.execute('DROP database fast_api_db;')
conn.commit()
cur.close()
conn.close()
