import requests

def check_hibp(email):
    print(f"\n[+] Checking HIBP for: {email}")
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    headers = {
        "User-Agent": "LeakCheckerBossScript",
        "hibp-api-key": "YOUR_HIBP_API_KEY"  # Optional if you have one
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        breaches = response.json().get("Breaches", [])
        if breaches:
            print(f"\t[!] Found {len(breaches)} breaches!")
            for breach in breaches:
                print(f"\t-> {breach['Name']} on {breach['BreachDate']}\n\t   Exposed: {', '.join(breach['DataClasses'])}")
        else:
            print("\t[-] No breaches found on HIBP.")
    elif response.status_code == 404:
        print("\t[-] No breaches found (404). Safe for now.")
    else:
        print(f"\t[!] Error: {response.status_code} - {response.reason}")

# def check_leakcheck(email):
#     print(f"\n[+] Checking LeakCheck.io for: {email}")
#     url = "https://leakcheck.io/api"
#     params = {
#         "key": "YOUR_LEAKCHECK_API_KEY",
#         "check": email,
#         "type": "email"
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         if data['found']:
#             print(f"\t[!] Found {data['found']} leaks!")
#             print(f"\t   Passwords exposed? {data['passwords']}")
#         else:
#             print("\t[-] No leaks found on LeakCheck.")
#     else:
#         print(f"\t[!] Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    user_email = input("Enter the email address to check for breaches: ").strip()
    check_hibp(user_email)
    # check_leakcheck(user_email)
    print("\n[*] Tip: Don’t reuse passwords. Use 2FA or Passkeys whenever possible.")
