import telebot
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from jamil_bot.forms import VehicleModelForm
from jamil_bot.models import VehicleModel

bot = telebot.TeleBot("5180471767:AAFWq1Z8Qd-ldeNbBJmqJaeCSlrddyIdueY")

#
# @bot.message_handler(commands=['start'])
# def start(message):
#     vehicles = VehicleModel.objects.all()
#     print(vehicles)
#
#     bot.reply_to(message, 'hello world')


def createjamilbot(request):
    if request.method == 'POST':
        form = VehicleModelForm(request.POST)

        if form.is_valid():
            bot.send_message(58939309, 'jamil zor bola')
            form.save()

        return redirect('/')

    else:
        form = VehicleModelForm()

        context = {
            'form': form
        }

        return render(request, 'index.html', context)


class HomeView(TemplateView):
    template_name = 'index.html'


bot.polling()
