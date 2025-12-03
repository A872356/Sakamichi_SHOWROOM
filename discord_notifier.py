import requests
import os

def send_notification(member_name, room_id, m3u8_url):
    """Sends  Discord notification: Announcement and M3U8 link."""
    
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    
    if not webhook_url:
        print("Error: DISCORD_WEBHOOK_URL not found in environment variables.")
        return False

    showroom_url = f"https://www.showroom-live.com/{room_id}"
    
    # --- Message 1: Announcement and Link ---
    content_announcement = (
        f"{member_name} is on live!\n"
        f"{showroom_url}"
    )
    
    payload_1 = {
        "content": content_announcement
    }
    
    # --- Message 2: M3U8 Link  ---
    content_m3u8 = f"<{m3u8_url}>"
    
    payload_2 = {
        "content": content_m3u8
    }
    
    try:
        # Send first message
        response_1 = requests.post(webhook_url, json=payload_1, timeout=10)
        response_1.raise_for_status()

        # Send second message
        response_2 = requests.post(webhook_url, json=payload_2, timeout=10)
        response_2.raise_for_status()
        
        print(f"Successfully sent Discord notification for {member_name}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Discord notification: {e}")
        return False