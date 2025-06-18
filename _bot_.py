import os,time
from aiogram import *
from _class_hunt_ import *

conex = Bot('6925848426:AAFfDLHcvTNY9Qq2_xCDiM7wUr-BHtVjnf0', parse_mode='html')
rex=Dispatcher(conex)

@rex.message_handler(commands=['start'])
async def start(msg):
    hi = await msg.reply('<code>code by :</code>𝗧𝗵𝗲𝗪𝗼𝗿𝗹𝗱𝘀𝗔𝗽𝗶𝘀「🐉」')
    time.sleep(1.5)
    name = msg['from']['first_name']
    await hi.edit_text(f'<b>wellcome </b>{name}')

@rex.message_handler(commands=['query'])
async def start(msg):
    query = msg.text[len('/query '):]
    
    if not query: return await msg.reply('<b> _use : <code>/query keywords</code></b>')
    else:
        unix  = GoogleQuey(query).getbs4()
        urls  = []
        for links in unix:
            url = links['href']
            if url.startswith('/url?q='):
                url = url[7:].split('&')[0] 
                if 'google' not in url and url not in urls: urls.append(url)

        if not urls: return await msg.reply('<b>No se encontro busqueda</b>\n')
        
        hola = await msg.reply('<code>__:google</code>')
        msgg = '<b>[⚡️] __Web Pages</b>\n'
        await hola.edit_text(msgg)

        msgg += """<b>
[•]Serve   [•]powered-by
[•]stripe  [•]squareup
━━━━━━

</b>"""
        await hola.edit_text(msgg)
        for url in urls:
            time.sleep(0.5)
            if "q%3D" in url: 
                msgg += '\n<b>Url : q%3D - asegurate que todas las palabres esten bien\n━━━━━━</b>\n'
                await hola.edit_text(msgg)
            else:
                resp = requt(urlsa=url)
                msgg += f"""<b>[🌵] Url :<code>{url}</code>
[•]{resp.clou()}          [•]{resp.Shopify()}
[•]{resp.stripe()}          [•]{resp.squareup()}
━━━━━━</b>
<code>code by :</code>𝗧𝗵𝗲𝗪𝗼𝗿𝗹𝗱𝘀𝗔𝗽𝗶𝘀「🐉」
"""
            try:
                await hola.edit_text(msgg)
            except:None
        
        msgg += '\n<b>__:Finished:__</b>'
        await hola.edit_text(msgg)

                


@rex.message_handler(commands=['url'])
async def start(msg):
    urls = msg.text[len('/url '):]
    
    if not urls: return await msg.reply('<b> _use : <code>/url Page</code></b>')
    else:
        if "q%3D" in urls: 
         
            await msg.reply('<b>Url : q%3D - asegurate que todas las palabres esten bien\n━━━━━━</b>')

        else:
            resp = requt(urlsa=urls)
            msgg = f"""<b>[🌵] Url :<code>{urls}</code>

[•]Serve : {resp.clou()}          [•]powered-by: {resp.Shopify()}
[•]Stripe: {resp.stripe()}          [•]squareup: {resp.squareup()}
━━━━━━</b>
<code>code by :</code>𝗧𝗵𝗲𝗪𝗼𝗿𝗹𝗱𝘀𝗔𝗽𝗶𝘀「🐉」
"""
            try:
                await msg.reply(msgg)
            except:None



os.system('clear')
print('__Onli: True')
executor.start_polling(rex)
