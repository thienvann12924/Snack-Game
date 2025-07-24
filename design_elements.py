# this is like Library of design elements made by Me
# creating all design elements in this file like buttons and tabs
import pygame
from pygame import Vector2


# font  = pygame.font.Font('Fonts/Pixeltype.ttf',25)

class Button:
    def __init__(self, x, y, font, hover_on=False, text='Button', color=(14, 75, 37), text_color=(255, 255, 255)):
        self.color = color
        self.text_color = text_color
        self.x = x
        self.y = y
        self.hover_on = hover_on
        self.font = font
        self.button_text(text)

    def button_text(self, text):
        self.text = text
        self.create_surface_and_rect()

    def create_surface_and_rect(self):
        self.text_surface = self.font.render(str(self.text), True, self.text_color)
        self.text_rect = self.text_surface.get_rect(topleft=(self.x + 5, self.y + 5))
        self.button_rect = pygame.Rect(self.x, self.y, self.text_rect.width + 10, self.text_rect.height + 10)

    def draw(self, screen, mouse=None, hover_color=None):
        if (not self.hover_on) or hover_color == None or (not self.button_rect.collidepoint(mouse)):
            pygame.draw.rect(screen, self.color, self.button_rect)
            screen.blit(self.text_surface, self.text_rect)
        else:
            self.hover_color = hover_color
            if mouse != None and self.button_rect.collidepoint(mouse):
                pygame.draw.rect(screen, self.hover_color, self.button_rect)
                screen.blit(self.text_surface, self.text_rect)
                return True
        self.screen = screen
        return False

    def get_button_rect(self):
        return self.button_rect

    def is_mouse_over(self, mouse):
        if self.button_rect.collidepoint(mouse):
            return True
        return False

    def get_button_text(self):
        return self.text


# tab will create basic template with different buttons
class Tab:
    def __init__(self, x, y, width, height, num_of_elements, spacing, font, border_color=(0, 0, 255), title='Tab'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.num_of_elements = num_of_elements
        self.border_color = border_color
        self.title = title
        self.itemLs = []
        self.font = font
        self.spacing = int(spacing)
        self.visible = False
        self.toggle = []
        self.toggle_text = []
        self.button_state = []
        self.closeButton = None
        self.button_list = []

    def add_item(self, Label, Btn_name='Button'):
        self.itemLs.append({'Label': str(Label), 'Name': str(Btn_name)})
        self.toggle.append(False)
        self.toggle_text.append(None)
        self.button_state.append(False)

    def update_item(self, index, Label, Btn_name='Button'):
        if index in range(len(self.itemLs)):
            self.itemLs[index] = {'Label': str(Label), 'Name': str(Btn_name)}

    def set_toggle_button(self, index, toggle_text):
        if index in range(len(self.itemLs)):
            self.toggle[index] = True
            self.toggle_text[index] = str(toggle_text)

    def toggle_button(self, index):
        if self.toggle[index]:
            if self.toggle_text != self.itemLs[index]['Name']:
                prev_text = self.itemLs[index]['Name']
                self.update_item(index, self.itemLs[index]['Label'], self.toggle_text[index])
                self.toggle_text[index] = prev_text
                # this will change button state to on
                self.button_state[index] = not self.button_state[index]

    def set_visibility(self, value=False):
        self.visible = value

    def draw(self, screen, mouse):
        if not self.visible:
            return

        self.button_list = []
        self.Label_list = []
        self.Label_rect_list = []
        self.title = self.font.render(str(self.title), True, (0, 0, 255))
        self.totalwidth = self.width + 20
        self.totalheight = self.y
        for item in self.itemLs:
            label = self.font.render(item['Label'], True, (255, 255, 255))
            label_rect = label.get_rect(topleft=(self.x + 10, self.totalheight + 10 + self.spacing))
            self.Label_list.append(label)
            self.Label_rect_list.append(label_rect)

            if label_rect.width + 40 > self.totalwidth:
                self.totalwidth = label_rect.width + 40

            self.totalheight += label_rect.height + 20 + self.spacing

            button = Button(self.x + 20, self.totalheight + 10, self.font, True, item['Name'], (100, 70, 20))
            self.button_list.append(button)

            button_rect = button.get_button_rect()

            if button_rect.width + 20 > self.totalwidth:
                self.totalwidth = button_rect.width + 20

            self.totalheight += button_rect.height

        self.Frame = pygame.Rect(self.x, self.y, self.totalwidth, self.totalheight)
        pygame.draw.rect(screen, (100, 78, 90), self.Frame)
        pygame.draw.rect(screen, self.border_color, self.Frame, 3)

        self.closeButton = Button(self.Frame.right - 25, self.Frame.top + 8, self.font, True, 'X')
        self.closeButton.draw(screen, mouse, (220, 10, 20))

        for i in range(len(self.Label_list)):
            screen.blit(self.Label_list[i], self.Label_rect_list[i])

        for button in self.button_list:
            button.draw(screen, mouse, (20, 220, 10))

    def close_button_clicked(self, mouse_position):
        if self.closeButton == None:
            return
        if self.closeButton.is_mouse_over(mouse_position):
            self.close_tab()

    def close_tab(self):
        self.visible = False

    def check_button_clicked(self, mouse_position):
        for index, button in enumerate(self.button_list):
            if button.is_mouse_over(mouse_position):
                self.toggle_button(index)

    # this will return the state of button
    def get_buttom_state(self, index):
        if int(index) in range(len(self.button_state)):
            return self.button_state[index]
        return None


class ArrowButtons:
    def __init__(self, x, y, font, box_size, button_color=(0, 0, 255), text_color=(255, 255, 255)):
        self.x = x;
        self.y = y;
        self.box_size = box_size;
        self.button_color = button_color;
        self.text_color = text_color
        self.get_buttons_rects(x, y, box_size)

    def get_buttons_rects(self, x, y, box_size):
        button_size = box_size // 3
        self.up_btn_rect = pygame.Rect(x + button_size, y, button_size, button_size)
        self.down_btn_rect = pygame.Rect(x + button_size, y + button_size * 2, button_size, button_size)
        self.left_btn_rect = pygame.Rect(x, y + button_size, button_size, button_size)
        self.right_btn_rect = pygame.Rect(x + button_size * 2, y + button_size, button_size, button_size)
        self.Button_Rect_tupple = (self.up_btn_rect, self.down_btn_rect, self.left_btn_rect, self.right_btn_rect)

    def draw_keys(self, screen, visibility=False):
        self.visibility = visibility
        if visibility:
            for button in self.Button_Rect_tupple:
                pygame.draw.rect(screen, self.button_color, button)

    def check_button_clicked(self, mouse_position):
        if not self.visibility:
            return
        for index, button in enumerate(self.Button_Rect_tupple):
            if button.collidepoint(mouse_position):
                if index == 0:
                    return Vector2(0, -1)
                elif index == 1:
                    return Vector2(0, 1)
                elif index == 2:
                    return Vector2(-1, 0)
                elif index == 3:
                    return Vector2(1, 0)


pygame.init()
