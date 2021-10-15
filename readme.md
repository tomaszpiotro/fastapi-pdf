fastapi-pdf
====

Service for generating pdf documents. Documents are defined using html and Jinja templates.
-----------

### Running

```bash
docker-compose up
```

Example
-----------

```bash
curl http://localhost:8000/pdf-template-example?first_name=Jane&last_name=Doe&first_consent=true >> statute.pdf
```
will generate pdf with first consent checked and first and last name completed:

![Pdf example](http://i.imgur.com/bXqvOL3.png)
