import argparse

def colored_print(color, msg):
    print(f'{color}{msg}\033[0m')

def search(username, websites):
    colored_print('\033[92m', f'[+] Searching for username: {username}')

    results = []

    for site in websites:
        url = site.format(username=username)
        results.append(url)

    for result in results:
        colored_print('\033[93m', f'{result}')

    colored_print('\033[92m', 'FINISHED: All website URLs printed.')

    save_results = input('\033[95mDo you want to save the results to a file? (y/n): \033[0m')

    if save_results.lower() == 'y':
        output_file = input('\033[95mEnter the output file name (e.g., example.txt): \033[0m')
        with open(output_file, 'w') as f:
            f.write('\n'.join(results))
        colored_print('\033[92m', f'All website URLs written to {output_file}')
    else:
        colored_print('\033[92m', 'Results not saved.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for a username on various websites')
    parser.add_argument('username', type=str, help='Username to search')
    args = parser.parse_args()

    websites = [
        'https://www.instagram.com/{username}',
        'https://www.facebook.com/{username}',
        'https://twitter.com/{username}',
        'https://www.youtube.com/@{username}',
        'https://www.tiktok.com/@{username}',
        'https://t.me/{username}',
        'https://www.snapchat.com/add/{username}',
        'https://threads.net/{username}',
        'https://www.reddit.com/user/{username}',
        'https://www.pinterest.com/{username}',
        'https://open.spotify.com/user/{username}',
        'https://www.roblox.com/user.aspx?username={username}',
        'https://www.wattpad.com/user/{username}',
        'https://linktr.ee/{username}'
    ]

    search(args.username, websites)
