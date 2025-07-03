# runs.py - Create thread + run with status polling

import requests
import time

def create_thread_and_run(client, assistant_id, prompt, max_checks=30):
    url = f"{client.base_url}/threads/runs"
    payload = {
        "assistant_id": assistant_id,
        "thread": {
            "messages": [{"role": "user", "content": prompt}]
        }
    }

    # Launch run
    resp = requests.post(url, headers=client.headers, json=payload)
    resp.raise_for_status()
    data = resp.json()
    run_id = data["id"]
    thread_id = data["thread_id"]

    print(f"🧵 Thread ID : {thread_id}")
    print(f"🚀 Run ID launched : {run_id}")

    # Wait for run to complete
    for i in range(max_checks):
        status_url = f"{client.base_url}/threads/{thread_id}/runs/{run_id}"
        r = requests.get(status_url, headers=client.headers)
        r.raise_for_status()
        status = r.json().get("status")
        if status == "completed":
            print(f"✅ Run completed after {i+1} checks.")
            break
        time.sleep(1)
    else:
        print("⚠️ Run did not complete in time.")

    return {"thread_id": thread_id, "run_id": run_id}
