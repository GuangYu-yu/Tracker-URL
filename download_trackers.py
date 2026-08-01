import requests
from urllib.parse import urlparse
import asyncio
import aiohttp
import zipfile
import io
import os
from bs4 import BeautifulSoup
import re

# 定义tracker链接列表
tracker_urls = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ws.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/refs/heads/master/all.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/refs/heads/master/http.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/refs/heads/master/nohttp.txt",
    "https://raw.githubusercontent.com/1265578519/OpenTracker/refs/heads/master/tracker.txt",
    "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all.txt",
    "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all_udp.txt",
    "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all_http.txt",
    "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all_https.txt",
    "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all_ws.txt",
    "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all_ip.txt"
]

# 新增的zip文件链接
zip_url = "https://gitee.com/harvey520/top.yaozuopan/raw/master/web/iplist.txt.zip"

# newtrackon.com 链接
newtrackon_url = "https://newtrackon.com/"

# tracker.cl 链接
tracker_cl_url = "https://tracker.cl/"

# tinytorrent.net 链接
tinytorrent_url = "https://tinytorrent.net/best-torrent-tracker-list-updated/"

# torrenttrackerlist.com 链接
torrenttrackerlist_url = "https://www.torrenttrackerlist.com/torrent-tracker-list/"

async def download_tracker(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                return content.strip().split('\n')
    except Exception as e:
        print(f"下载 {url} 时发生错误: {e}")
    return []

async def download_zip_tracker(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                with zipfile.ZipFile(io.BytesIO(content)) as zip_file:
                    txt_files = [f for f in zip_file.namelist() if f.endswith('.txt')]
                    if txt_files:
                        with zip_file.open(txt_files[0]) as txt_file:
                            return txt_file.read().decode('utf-8').strip().split('\n')
    except Exception as e:
        print(f"下载或处理zip文件 {url} 时发生错误: {e}")
    return []

async def download_newtrackon(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                trackers = []
                for row in soup.find_all('tr'):
                    cells = row.find_all('td')
                    if len(cells) >= 2:
                        tracker_url = cells[0].text.strip()
                        uptime = cells[1].text.strip().rstrip('%')
                        try:
                            if float(uptime) >= 50.00:
                                trackers.append(tracker_url)
                        except ValueError:
                            continue
                return trackers
    except Exception as e:
        print(f"从 {url} 下载或处理 tracker 时发生错误: {e}")
    return []

async def download_tracker_cl(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                trackers = []
                
                # 查找 Current tracker address
                current_tracker = soup.find('p', string='Current tracker address:')
                if current_tracker and current_tracker.find_next('p'):
                    tracker_url = current_tracker.find_next('p').strong.text.strip()
                    trackers.append(tracker_url)
                
                # 查找 Mirror / Old address
                mirror_tracker = soup.find('p', string='Mirror / Old address:')
                if mirror_tracker and mirror_tracker.find_next('p'):
                    tracker_url = mirror_tracker.find_next('p').strong.text.strip()
                    trackers.append(tracker_url)
                
                return trackers
    except Exception as e:
        print(f"从 {url} 下载或处理 tracker 时发生错误: {e}")
    return []

async def download_tinytorrent(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                trackers = []
                pre_tags = soup.find_all('pre')
                for pre in pre_tags:
                    tracker_urls = re.findall(r'(udp://\S+|http://\S+|https://\S+|ws://\S+|wss://\S+)', pre.text)
                    trackers.extend(tracker_urls)
                return trackers
    except Exception as e:
        print(f"从 {url} 下载或处理 tracker 时发生错误: {e}")
    return []

async def download_torrenttrackerlist(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                trackers = []
                pre_tags = soup.find_all('pre', class_='customcodewords')
                for pre in pre_tags:
                    tracker_urls = re.findall(r'(udp://\S+|http://\S+|https://\S+|ws://\S+|wss://\S+)', pre.text)
                    trackers.extend(tracker_urls)
                return trackers
    except Exception as e:
        print(f"从 {url} 下载或处理 tracker 时发生错误: {e}")
    return []

async def main():
    all_trackers = set()

    async with aiohttp.ClientSession() as session:
        tasks = [download_tracker(session, url) for url in tracker_urls]
        tasks.append(download_zip_tracker(session, zip_url))
        tasks.append(download_newtrackon(session, newtrackon_url))
        tasks.append(download_tracker_cl(session, tracker_cl_url))
        tasks.append(download_tinytorrent(session, tinytorrent_url))
        tasks.append(download_torrenttrackerlist(session, torrenttrackerlist_url))
        results = await asyncio.gather(*tasks)

        for tracker_list in results:
            all_trackers.update(tracker_list)

    # 去除空行和重复项
    cleaned_trackers = sorted(set(filter(bool, all_trackers)))

    # 保存到文件
    with open('all.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_trackers))

    print(f"合并后的tracker数量: {len(cleaned_trackers)}")
    print("已保存到 all.txt")

if __name__ == "__main__":
    asyncio.run(main())
