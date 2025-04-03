import logging
import sys
import time
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

# Configurações
ACCESS_ID = ""
ACCESS_KEY = ""
API_ENDPOINT = ""
DEVICE_ID = ""

# Códigos FIXOS para Smart Zinnia
POWER_CODE = "switch_led"
BRIGHTNESS_CODE = "bright_value_v2"
WORK_MODE_CODE = "work_mode"

class ZinniaController:
    def __init__(self):
        TUYA_LOGGER.setLevel(logging.INFO)
        self.api = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
        self.api.connect()
        logging.info("Conexão estabelecida com a lâmpada Smart Zinnia")

    def _send_command(self, commands):
        """Envio otimizado de comandos com tratamento de erro"""
        try:
            response = self.api.post(
                f'/v1.0/iot-03/devices/{DEVICE_ID}/commands',
                {'commands': commands}
            )
            if not response.get('success', False):
                logging.error(f"Erro na resposta: {response}")
                return False
            return True
        except Exception as e:
            logging.error(f"Falha de comunicação: {str(e)}")
            return False

    def set_brightness(self, percent):
        """Ajusta brilho com validação"""
        if percent < 0 or percent > 100:
            print("Erro: Brilho deve ser entre 0% e 100%")
            return False

        value = int(1000 * percent / 100)
        commands = [
            {'code': POWER_CODE, 'value': True},
            {'code': BRIGHTNESS_CODE, 'value': value},
            {'code': WORK_MODE_CODE, 'value': 'white'}
        ]
        return self._send_command(commands)

    def turn_on(self, brightness=None):
        """Liga com brilho opcional"""
        if brightness is not None:
            return self.set_brightness(brightness)
        return self._send_command([{'code': POWER_CODE, 'value': True}])

    def turn_off(self):
        """Desliga a lâmpada"""
        return self._send_command([{'code': POWER_CODE, 'value': False}])

    def toggle(self):
        """Alterna entre ligado/desligado"""
        status = self.api.get(f"/v1.0/iot-03/devices/{DEVICE_ID}/status")
        if status and status.get('success', False):
            is_on = any(item['value'] for item in status['result']
                       if item['code'] == POWER_CODE)
            return self.turn_off() if is_on else self.turn_on()

def show_menu():
    """Exibe o menu interativo"""
    print("\n" + "="*30)
    print("  CONTROLE SMART ZINNIA  ")
    print("="*30)
    print("1. Ligar")
    print("2. Desligar")
    print("3. Brilho Máximo (100%)")
    print("4. Brilho Médio (50%)")
    print("5. Brilho Mínimo (10%)")
    print("6. Brilho Personalizado")
    print("7. Rotina Automática")
    print("8. Alternar Estado (Toggle)")
    print("9. Sair")
    print("="*30)

def run_automatic_routine(controller):
    """Executa rotina automática de acordar"""
    print("\nIniciando rotina matinal...")
    for percent in range(10, 101, 10):
        print(f"⏳ Ajustando brilho para {percent}%...")
        controller.set_brightness(percent)
        time.sleep(10)  # Intervalo de 30 segundos
    print("✅ Rotina concluída!")

def main():
    controller = ZinniaController()

    # Modo linha de comando
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        try:
            if arg == 'on':
                if len(sys.argv) > 2:
                    controller.turn_on(int(sys.argv[2]))
                else:
                    controller.turn_on()
            elif arg == 'off':
                controller.turn_off()
            elif arg.isdigit():
                controller.set_brightness(int(arg))
            elif arg == 'routine':
                run_automatic_routine(controller)
            else:
                print("Comandos válidos: on [0-100], off, [0-100], routine")
        except ValueError:
            print("Por favor, insira um valor numérico para o brilho")
        return

    # Modo interativo
    while True:
        show_menu()
        choice = input("Escolha (1-9): ")

        try:
            if choice == '1':
                if controller.turn_on():
                    print("✅ Lâmpada ligada")
            elif choice == '2':
                if controller.turn_off():
                    print("✅ Lâmpada desligada")
            elif choice == '3':
                if controller.set_brightness(100):
                    print("✅ Brilho máximo ativado")
            elif choice == '4':
                if controller.set_brightness(50):
                    print("✅ Brilho médio ativado")
            elif choice == '5':
                if controller.set_brightness(10):
                    print("✅ Brilho mínimo ativado")
            elif choice == '6':
                try:
                    value = int(input("Digite o brilho (0-100%): "))
                    if controller.set_brightness(value):
                        print(f"✅ Brilho ajustado para {value}%")
                except ValueError:
                    print("❌ Valor inválido! Use números de 0 a 100")
            elif choice == '7':
                run_automatic_routine(controller)
            elif choice == '8':
                if controller.toggle():
                    print("✅ Estado alternado")
            elif choice == '9':
                print("Saindo...")
                break
            else:
                print("❌ Opção inválida!")
        except Exception as e:
            print(f"❌ Erro: {str(e)}")

        time.sleep(1)  # Pequeno delay entre comandos

if __name__ == "__main__":
    main()
