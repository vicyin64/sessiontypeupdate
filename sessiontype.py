import requests

# Step 1: Replace 'YOUR_ACCESS_TOKEN' with your actual Webex access token
access_token = 'YOUR_ACCESS_TOKEN'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Step 2: Fetch a list of all users in the organization
def get_all_users():
    users_url = 'https://api.ciscospark.com/v1/people'
    response = requests.get(users_url, headers=headers)

    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f"Failed to retrieve users: {response.status_code}")
        return []

# Step 3: Update session type for each user
def update_session_type(site_url, user_id, new_session_type):
    update_url = f'https://api.ciscospark.com/v1/admin/meeting/userconfig/sessionTypes'
    data = {
	'siteUrl': site_url,
        'personId': user_id,
        'sessionTypeIds': new_session_type
    }
    response = requests.put(update_url, json=data, headers=headers)

    if response.status_code == 200:
        print(f"Session type updated for user {user_id}")
    else:
        print(f"Failed to update session type for user {user_id}: {response.status_code}")

def main():
    # Step 1: Authenticate and get access token
    # (Already provided in 'access_token' variable)

    # Step 2: Set your Webex site URL
    site_url = 'YOUR_SITE_URL'

    # Step 3: Get all users in the organization
    users = get_all_users()

    # Step 4: Update session type for each user in format ["3","9","11","13","659","687"]
    new_session_type = [YOUR_SESSIONTYPE_ARRAY]
    for user in users:
        user_id = user['id']
        update_session_type(site_url, user_id, new_session_type)

if __name__ == "__main__":
    main()
