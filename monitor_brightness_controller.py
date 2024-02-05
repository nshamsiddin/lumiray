import screen_brightness_control as sbc
import keyboard

class MonitorBrightnessController:
    def set_brightness(self, brightness):
        """Set the brightness of all detected monitors."""
        sbc.set_brightness(brightness)

    def get_brightness(self):
        """Get the average brightness of all detected monitors."""
        return sbc.get_brightness()
