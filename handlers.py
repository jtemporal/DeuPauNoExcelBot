from bottery import handlers

import views

msghandlers = [
    handlers.startswith('/replyshrug', views.reply_shrug),
    handlers.startswith('/shrug', views.shrug)
]
