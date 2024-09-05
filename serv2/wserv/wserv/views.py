import json
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def run_command(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        command = data.get('command')
        channel_layer = get_channel_layer()
        print(command)
        async_to_sync(channel_layer.group_send)(
            "client_group",
            {
                "type": "receive",
                "message": command,
            },
        )
        return JsonResponse({"result": "Command sent"}, status=200)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)