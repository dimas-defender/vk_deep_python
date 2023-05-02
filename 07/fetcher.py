from sys import argv
import asyncio
import aiohttp


async def fetch_url(url, session):
    async with session.get(url) as resp:
        assert resp.status == 200
        data = await resp.read()
        assert data is not None
        print(f'{url[:-1]} handled')


async def start_worker(queue, session):
    while True:
        url = await queue.get()

        try:
            await fetch_url(url, session)
        except Exception as err:
            print(f'ERROR with {url}: {err}')
        finally:
            queue.task_done()


async def fetch_batch(urls, n_workers, session):
    queue = asyncio.Queue()

    workers = [
        asyncio.create_task(start_worker(queue, session))
        for _ in range(n_workers)
    ]

    for url in urls:
        await queue.put(url)

    await queue.join()

    for worker in workers:
        worker.cancel()


async def main(urls, workers):
    async with aiohttp.ClientSession() as session:
        await fetch_batch(urls, workers, session)


if __name__ == '__main__':
    with open(argv[2], 'r') as urls:
        asyncio.run(main(urls, int(argv[1])))