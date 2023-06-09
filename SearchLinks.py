import requests
from bs4 import BeautifulSoup


url_base = 'https://doxbin.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Cookie": "__ddg1_=HBaDYHTwDj8JtiDQuu6L; vDDoS=672567fbefd293529e5ca870e2c2b570; XSRF-TOKEN=eyJpdiI6IjMrNkdERGhDTk1jaHFBd0ZDbnJhWVE9PSIsInZhbHVlIjoieTN6b1o4NHZRcVY3UXltUm5qeDlETURucGFMMW1uNVRZcmdEXC9oS3g5NzNCenFjNFYxWnJkYlREdmJhM2pwUlkiLCJtYWMiOiJkMzZiNTRmYzUwMDZiMjE4OTFmODM3ZTI5ZGUyOWE4NTA3YjQ4OWJhYTY0NjA0OGJkMjhhYmJkN2RkY2RmZjM4In0%3D; doxbin_session=eyJpdiI6IjhXYndWdVwvcmJ2czN6dnY0Y1hHTXF3PT0iLCJ2YWx1ZSI6ImE4NjdiNWphQ01ZcUk5Zk5salE0ZlpnT210Tkk5T3F4dFhrU0x0YlVodXZHVmFCcExqNFJTa3FyUzRjRjhPUUciLCJtYWMiOiIxZWNhNTQ0Njc5ZTBmZDhjMmY0YWZhNTg2N2E4YzQ1ZWQyYWNiNWFkZDkxNjVmMmY5Y2RmMTI4N2M2OWQ3NDhjIn0%3D"
}

response = requests.get(url_base, headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

list_url = []

for link in soup.find_all('a'):

    if 'C2' in str(link.get('href')):
        
        list_url.append(str(link.get('href')))
        print(f"ADD: {str(link.get('href'))}")
        