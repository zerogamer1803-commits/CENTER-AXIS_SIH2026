import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Energy, EnergyHistory


def energy_list(request):
    """Return current solar and footstep energy data."""
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET method required'},
            status=405
        )

    data = []

    for energy in Energy.objects.all():
        data.append({
            'source': energy.source,
            'power_output': energy.power_output,
            'solar_voltage': energy.solar_voltage,
            'energy_today': energy.energy_today,
            'energy_week': energy.energy_week,
            'energy_month': energy.energy_month,
            'efficiency': energy.efficiency,
            'peak_power': energy.peak_power,
            'timestamp': energy.timestamp.isoformat(),
        })

    return JsonResponse({
        'count': len(data),
        'data': data
    })


def energy_history(request):
    """Return historical energy generation data."""
    if request.method != 'GET':
        return JsonResponse(
            {'error': 'GET method required'},
            status=405
        )

    records = EnergyHistory.objects.all()

    data = []

    for record in records:
        data.append({
            'source': record.source,
            'energy': record.energy,
            'date': record.date.isoformat(),
            'timestamp': record.timestamp.isoformat(),
        })

    return JsonResponse({
        'count': len(data),
        'data': data
    })


@csrf_exempt
def solar_voltage_update(request):
    """Receive solar voltage from ESP32."""

    if request.method != 'POST':
        return JsonResponse(
            {'error': 'POST method required'},
            status=405
        )

    try:
        data = json.loads(request.body)

        voltage = float(data.get('solar_voltage'))

        solar = Energy.objects.get(source='Solar')

        solar.solar_voltage = voltage
        solar.save()

        return JsonResponse({
            'success': True,
            'solar_voltage': round(voltage, 2)
        })

    except Energy.DoesNotExist:
        return JsonResponse(
            {'error': 'Solar energy record not found'},
            status=404
        )

    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse(
            {'error': 'Invalid solar voltage'},
            status=400
        )