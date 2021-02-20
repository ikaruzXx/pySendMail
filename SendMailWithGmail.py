import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
contenido = """ Hola,esto es un simple correo.Es solo texto"""

# Credenciales del correo
emisor_address = 'xxx@gmail.com'
emisor_pass = 'xxxxxx'
receptor_address = 'xxx@gmail.com'

# setup the MIME
message = MIMEMultipart()
message['From'] = emisor_address
message['To'] = receptor_address
message['Subject'] = 'Test con python 3'

# cuerpo del correo
message.attach(MIMEText(contenido, 'plain'))

# Crear una sesion para enviar el correo
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(emisor_address, emisor_pass)
text = message.as_string()
session.sendmail(emisor_address, receptor_address, text)
session.quit()
print('Correo enviado')
