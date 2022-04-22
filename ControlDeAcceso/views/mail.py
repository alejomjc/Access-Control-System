from django.template.loader import get_template
from django.core.mail import EmailMessage


def enviar_correo(contenido):
    plantilla = get_template('Mail/template.html')
    email = EmailMessage(
        contenido['asunto'],
        plantilla.render(contenido),
        '"CDA" <bluestacksdealejo@gmail.com>',
        [],
        contenido['lista_destinatarios']
    )
    email.content_subtype = "html"
    email.send()
