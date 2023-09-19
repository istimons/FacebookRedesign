""" 
This is a Facebook redesign ceoncept using KivyMD.

Fork it & try to see if adding some database between users from firebase can fire some Notifications, Good Luck!


Developed by lord istimons
"""

import kivy

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty, StringProperty, OptionProperty, DictProperty, BooleanProperty
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
import database.database
from database.database import profiles
from kivymd.uix.card import MDCard
from kivy.clock import Clock







from kivy.logger import Logger, LOG_LEVELS
Logger.setLevel(LOG_LEVELS['debug'])

import os
file_path = 'assets/videos'
if os.path.exists(file_path):
    pass
esle:print('Not Found!')





Builder.load_file('kivy/pages/log_in_screen.kv')
Builder.load_file('kivy/pages/org_login_screen.kv')
Builder.load_file('kivy/pages/user_log_in_screen.kv')
Builder.load_file('kivy/pages/menu_tab_screen.kv')
Builder.load_file('kivy/pages/blog_posting_screen.kv')
Builder.load_file('kivy/widgets/story_layout.kv')
Builder.load_file('kivy/widgets/avatar.kv')
Builder.load_file('kivy/widgets/post_content_items.kv')
Builder.load_file('kivy/widgets/bottom_post_content_bar_items.kv')
Builder.load_file('kivy/widgets/friends_layout.kv')
Builder.load_file('kivy/widgets/video_post_items.kv')
Builder.load_file('kivy/widgets/market_place_layout.kv')
Builder.load_file('kivy/widgets/notifications_layout.kv')
Builder.load_file('kivy/widgets/chat_action.kv')
Builder.load_file('kivy/widgets/text_field.kv')
Builder.load_file('kivy/widgets/chat_list_item.kv')



class WindowManager(ScreenManager):
    ''' This is the parent screen for all the widgets, starting from screens '''
    

class MainScreen(Screen):
    ''' This class is the screen that will hold widgets that we are going to add to the main window
    WindowManager class which has the ScreenManager
    '''

class LogInScreen(Screen):
    ''' A class that all the Home items is built on '''
    

class OrganizationLogInScreen(Screen):
    ''' Custom  screen for organization Sign in '''

class IndividualLogInScreen(Screen):
    ''' Custom screen for Individual Sign in '''

class MenuTabScreen(Screen):
    ''' Custom screen for menu items'''

class FriendsTabScreen(Screen)    :
    ''' Custom screen for friends tab items'''


class ChatScreen(Screen):
    ''' Custom method for displaying blogs chats '''


class HomeTab(MDFloatLayout, MDTabsBase):
    ''' A tab that holds all the Facebook's Home screen content '''


class FriendsTap(MDFloatLayout, MDTabsBase):
    ''' A Custom Tab for holding friends tab '''


class VideoTab(MDFloatLayout, MDTabsBase):
    ''' A Custom Tab for holding video tab items '''


class MarketPlaceTab(MDFloatLayout, MDTabsBase):
    ''' A Custom Tab for holding marketplace tab items '''


class NotificationTab(MDFloatLayout, MDTabsBase):
    ''' A Custom Tab for holding notification tab items'''


class MenuTab(MDFloatLayout, MDTabsBase):
    ''' A Custom Tab for holding menu tab items'''


class StoryWithImage(MDBoxLayout):
    '''A horizontal layout with an image and a text(company's username) - The Story.'''

    text = StringProperty()
    source = StringProperty()


class FriendsLayout(MDBoxLayout):
    ''' Custom class for friend request timeline '''

    text = StringProperty()
    source = StringProperty()
    friend_request_initial_time = StringProperty()
    mutual_friends = StringProperty()
    image = ObjectProperty()

class NotificationLayout(MDBoxLayout):
    ''' Custom class for Notifications '''

    company_name = StringProperty()
    company_image = ObjectProperty()
    time_received = StringProperty()
    notification_content = StringProperty()


class MarketPlaceLayout(MDCard):
    ''' Custom class for marketplace content '''

    price = StringProperty()
    image_to_post = StringProperty()


class PostListItem(MDCard):
    '''A clickable post item for the post timeline.'''

    isRead = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting'])
    company_name = StringProperty()
    mssg = StringProperty()
    timestamp = StringProperty()
    company_avatar = StringProperty()
    profile = DictProperty()


class VideoPostListItem(MDCard):
    ''' Custom widget for videos per post '''

    isRead = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting'])
    company_name = StringProperty()
    mssg = StringProperty()
    timestamp = StringProperty()
    company_avatar = StringProperty()
    profile = DictProperty()
    company_video_dir = StringProperty()


class MessageScreen(Screen):
    '''
    A screen for displaying messages between friends 
    the class is used in the create_chat method, this methos uses message builder objects to override the 
    ChatAction class (below) for displaying a chatting area in the users chat screen

    '''

    text = StringProperty()
    image = ObjectProperty()
    active = BooleanProperty(default_value=False)


class ChatAction(MDBoxLayout):
    ''' 
    
    A chart area for users database .
    The buble is created in a different .kv file called chat_note.kv
    '''

    profile = DictProperty()
    message = StringProperty()
    time = StringProperty()
    sender = StringProperty()
    is_read = OptionProperty('waiting', options=['read', 'delivered', 'waiting'])


class ChatListItem(MDCard):
    """ 
    #2
    A chat Item holders for clicking to show database 
    Then create a database.py method to import the charts
    This is done by the chat_list_method() at the main app class
    
    """

    is_read = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting'])
    friend_name = StringProperty()
    message = StringProperty()
    time_stamp = StringProperty()
    friend_profile_avatar = StringProperty()
    profile = DictProperty()


class MainApp(MDApp):

    def build(self):

        #setting theme properties
        self.title = 'Facebook'
        self.theme_cls_style = 'Teal'  # App theme
        self.theme_cls.primary_palette = 'Teal' # Main color palette
        self.icon = 'assets/images/logo/logo.png'

        # other colors are 
        
        # 'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo',
        # 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber',
        # 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray'

        # Valid values for color palette selecting.
        # kivymd.color_definitions.hue = ['50', 100', '200', '300', '400', '500', '600', '700',
        # '800', '900', 'A100', 'A200', 'A400', 'A700']

        self.theme_cls.accent_palette = 'Teal' # Second color pallete given the hue value below
        self.theme_cls_accent_hue = '700' 

        # adding all the screens to the window manager
        self.wm = WindowManager(transition=FadeTransition())

        screens = [
            MainScreen(name='main_screen'), LogInScreen(name='log_in_screen'), OrganizationLogInScreen(name='org_login_screen'), IndividualLogInScreen(name='ind_log_in_screen'), MessageScreen(name='message_screen'), ChatScreen(name='chat_screen')
        ]

        for screen in screens:
            self.wm.add_widget(screen)

        self.story_builder()
        self.company_post_list_builder()
        self.company_top_post_items_builder()
        self.company_video_list_builder()
        self.friends_list_method()
        self.market_place_sales_method()
        self.notification_list_method()
        self.chat_list_method()

        self.wm.current  = "log_in_screen"
        # Clock.schedule

        return self.wm
    


    def switch_screen(self, screen):
        ''' A Custom switch to change a screen using Window Manager (wm) '''

        self.wm.current = screen

    def friends_list_method(self):
        ''' Custom method for showing friend & friend requests  '''

        for profile in database.database.profiles:
            self.friends_layout = FriendsLayout()
            self.friends_layout.text = profile['name']
            self.friends_layout.source = profile['image']
            self.friends_layout.mutual_friends = profile['mutual_friends']
            self.friends_layout.friend_request_initial_time = profile['friend_request_initial_time']
            self.wm.screens[0].ids['friends_layout'].add_widget(self.friends_layout)


    def notification_list_method(self):
        ''' Custom method for creating notifications'''

        for profile in profiles:
            for message in profile['msg']:
                
        # for profile in database.database.profiles:
                self.nofitification_layout = NotificationLayout()
                self.nofitification_layout.company_name = profile['name']
                self.nofitification_layout.company_image = profile['image']
                self.nofitification_layout.time_received = profile['time_received']


                lastmessage, time, isRead, sender = message.split(';')
                self.nofitification_layout.notification_content = lastmessage           
            self.wm.screens[0].ids['notifications_layout'].add_widget(self.nofitification_layout)


    def market_place_sales_method(self):
        ''' Cutom method that holds the marketplace items '''

        for profile in database.database.profiles:
            self.market_place_sales = MarketPlaceLayout()
            self.market_place_sales.price = profile['price']
            self.market_place_sales.image_to_post = profile['image_for_posting']
            self.wm.screens[0].ids['company_market_place_sales'].add_widget(self.market_place_sales)

    def story_builder(self):
        '''Create a Story for each user and adds it to the story layout'''
        for profile in database.database.profiles:
            self.story = StoryWithImage()
            self.story.text = profile['name']
            self.story.source = profile['image']
            self.wm.screens[0].ids['story_layout'].add_widget(self.story)
            
    def company_top_post_items_builder(self):
        ''' Custom method for creating each company with its own content displayed at the top of the app'''


    def company_post_list_builder(self):
        ''' custom method for building company posts from the database'''
        for messages in profiles:
            for message in messages['msg']:
                self.postitem = PostListItem()
                self.postitem.profile = messages
                self.postitem.company_name = messages['name']
                self.postitem.company_avatar = messages['image']

                lastmessage, time, isRead, sender = message.split(';')
                self.postitem.mssg = lastmessage
                self.postitem.timestamp = time
                self.postitem.isRead = isRead
                self.postitem.sender = sender
            self.wm.screens[0].ids['company'].add_widget(self.postitem)


    def company_video_list_builder(self):
        ''' Custom widget to videos/reels layout'''

        for messages in profiles:
            for message in messages['msg']:
                self.videpostitem = VideoPostListItem()
                self.videpostitem.profile = messages
                self.videpostitem.company_name = messages['name']
                self.videpostitem.company_avatar = messages['image']
                self.videpostitem.company_video_dir = messages['company_video_dir']

                lastmessage, time, isRead, sender = message.split(';')
                self.videpostitem.mssg = lastmessage
                self.videpostitem.timestamp = time
                self.videpostitem.isRead = isRead
                self.videpostitem.sender = sender
            self.wm.screens[0].ids['company_video'].add_widget(self.videpostitem)

    def create_chat(self, profile):
        ''' 
        getting all the messages from database.py module and creating a MessageScreen.
        in this case this file is used as the database. 
        You can use Firebase/PostgreSQl at this point to use messages from a remote server
        '''

        self.chat_screen = MessageScreen()
        self.message_builder(profile, self.chat_screen)
        self.chat_screen.text = profile['name']
        self.chat_screen.image = profile['image']
        self.chat_screen.active = profile['active']
        self.wm.switch_to(self.chat_screen)


    def message_builder(self, profile, screen):
        '''        
        creating a message notification for creating a chat
        the messages are in the database.py app which is a db alternative        
        '''

        for y_profile in profile['msg']:
            for messages in y_profile.split("~"):
                if messages != "":
                    message, time, is_read, sender = messages.split(";")
                    self.chat_message = ChatAction()
                    self.chat_message.message = message
                    self.chat_message.time = time
                    self.chat_message.is_read = is_read
                    self.chat_message.sender = sender
                    screen.ids['messagelist'].add_widget(self.chat_message)

    def chat_list_method(self):
        '''         
        
        method for adding database in the main screen via ChatListItem class (above using MDLabel) 
        the CHATLIST is sent to the UI by chatlist id in the .kv file where it is put inside 
        a ScrollView as shown below. The screen as the main widget (MainScreen class) is used to add the ChatListItem class
        to the UI.
        '''

        # accessing data from the database.py file (from a dictionary)

        for messages in profiles:
            for message in messages['msg']:
                self.chatitem = ChatListItem()
                self.chatitem.profile = messages
                self.chatitem.friend_name = messages['name']
                self.chatitem.friend_profile_avatar = messages['image']

                lastmessage, time, is_read, sender = message.split(';') # database to be separated where there are semi-colons(all database must be 4)
                self.chatitem.message = lastmessage
                self.chatitem.time_stamp = time
                self.chatitem.is_read = is_read
                self.chatitem.sender = sender
            # self.root.ids.bloglist.add_widget(self.chatitem)

if __name__=="__main__":

    MainApp().run()