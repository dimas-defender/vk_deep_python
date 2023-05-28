import argparse
import asyncio
import aiohttp


async def fetch_url(url, session):
    async with session.get(url) as resp:
        assert resp.status == 200
        data = await resp.read()  # print(data, file=)
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
    queue = asyncio.Queue(2 * n_workers)

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
    parser = argparse.ArgumentParser()
    parser.add_argument("workers", type=int)
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, 'r') as urls:
        asyncio.run(main(urls, args.workers))
