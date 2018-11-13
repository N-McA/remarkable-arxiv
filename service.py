
import aiohttp
import asyncio
from bs4 import BeautifulSoup

from pathlib import Path

from sanic import Sanic
from sanic.response import json

from sanic_cors import cross_origin

import subprocess


ARXIV_PAPER_URL_TEMPLATE = 'https://arxiv.org/abs/{paper_id}'
ARXIV_PDF_URL_TEMPLATE = 'https://arxiv.org/pdf/{paper_id}'

DATA_FOLDER = Path('arxiv-papers/')


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_filename(paper_id):

    url = ARXIV_PAPER_URL_TEMPLATE.format(paper_id=paper_id)

    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)

    soup = BeautifulSoup(html, 'html.parser')

    title_html = soup.select('h1.title.mathjax')[0]
    title_string = title_html.text
    assert title_string.startswith('Title:')
    title = title_string[len('Title:'):]

    new_file_name = title.replace(' ', '_') + '.pdf'

    return new_file_name


async def save_pdf_response(paper_id, fname):
    url = ARXIV_PDF_URL_TEMPLATE.format(paper_id=paper_id)
    headers = {
        "User-Agent": "Mozilla",
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, timeout=None) as response:
            if response.status == 200:
                pdf_data = await response.read()
                path = DATA_FOLDER / fname
                with path.open('wb') as out_file:
                    out_file.write(pdf_data)
                subprocess.call([
                    './crop-and-send-pdf-then-delete-all', str(path),
                ])
            else:
                raise Exception('Bad Response')


app = Sanic()


@app.route("/get-paper/<paper_id>")
@cross_origin(app)
async def test(request, paper_id):
    fname = await get_filename(paper_id)
    asyncio.ensure_future(save_pdf_response(paper_id, fname))
    return json({"paper_id": paper_id, "fname": fname})

if __name__ == "__main__":
    app.run(host="localhost", port=8006)
