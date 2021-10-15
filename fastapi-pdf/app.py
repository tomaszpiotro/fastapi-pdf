import os
from typing import Optional

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from weasyprint import HTML

debug = os.environ.get('DEBUG', False,)

app = FastAPI(debug=debug)


templates = Jinja2Templates(directory='templates')


class PdfResponse(Response):
    media_type = 'application/pdf'


@app.get('/html-template-example', response_class=HTMLResponse)
async def html_template_example(
    request: Request,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    email: Optional[str] = None,
    phone_number: Optional[str] = None,
    first_consent: bool = False,
    second_consent: bool = False,
    third_consent: bool = False,
    fourth_consent: bool = False,
):
    return templates.TemplateResponse(
        'example.html',
        {
            'request': request,
            'filename': 'statute.pdf',
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'first_consent': first_consent,
            'second_consent': second_consent,
            'third_consent': third_consent,
            'fourth_consent': fourth_consent,
        },
    )


@app.get('/pdf-template-example', response_class=PdfResponse)
async def html_template_example(
    request: Request,
    first_name: str = None,
    last_name: str = None,
    email: str = None,
    phone_number: str = None,
    first_consent: bool = False,
    second_consent: bool = False,
    third_consent: bool = False,
    fourth_consent: bool = False,
):
    html = templates.TemplateResponse(
        'example.html',
        {
            'request': request,
            'filename': 'statute.pdf',
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'first_consent': first_consent,
            'second_consent': second_consent,
            'third_consent': third_consent,
            'fourth_consent': fourth_consent,
        },
    ).body
    pdf_content = HTML(string=html).write_pdf()
    return PdfResponse(
        content=pdf_content, headers={'Content-Disposition': f'inline; filename=statute.pdf'})
