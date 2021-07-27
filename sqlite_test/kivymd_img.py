from kivymd.uix.behaviors import HoverBehavior
from kivy.cache import Cache
import threading
from types import SimpleNamespace as sn
from kivymd.uix.dialog import MDDialog
import os
from kivy.properties import *
import numpy as np
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.effectwidget import *
from kivy.properties import ColorProperty
from kivymd.utils.fitimage import FitImage
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty, ColorProperty
from kivy.uix.image import AsyncImage
from functools import partial
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.logger import Logger
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.video import video_ffpyplayer
from kivy.core.window import Window
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.video import Video
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RectangularElevationBehavior, FocusBehavior
from kivy.config import Config
from kivy.clock import mainthread
from kivy.core.text import LabelBase
from fake_headers import Headers
from random import choice
from random import randint as rd
from kivy.graphics import Color, Ellipse, Rectangle, RoundedRectangle
import requests
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
import io
Rectangle


class blur_image(EffectWidget, AsyncImage):
    effects = (HorizontalBlurEffect(size=2.0))


class op_button(Button):
    def __init__(self, **kwargs):
        super(op_button, self).__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]


class blImage(AsyncImage, HoverBehavior, ButtonBehavior):
    focus_behavior = BooleanProperty(True)
    object_poster = ObjectProperty()

    def on_enter(self):
        if self.focus_behavior:
            (label, image) = self.parent.children
            self.txt_ = image.color
            image.color = (0, 0, 0, 1)
            label.color = (1, 1, 1, 1)

    def on_leave(self):
        if self.focus_behavior:
            (label, image) = self.parent.children
            image.color = self.txt_
            label.color = (0, 0, 0, 1)


class MDCard_d(RelativeLayout, MDCard):
    id = StringProperty('')


def generate_card(image_src, title, id_t):
    mdcrd = RelativeLayout(size_hint=(None, 1), size=image_src.texture_size,
                           width=image_src.width, height=image_src.height,)
    MDBox1 = AnchorLayout(size=image_src.texture_size, width=image_src.width,
                          height=image_src.height, anchor_x='center', anchor_y='top')
    fI = image_src
    mdcrd.add_widget(MDBox1)
    MDBox1.add_widget(fI)
    bl = MDLabel(text=title,
                 halign="center", pos=image_src.pos, size=image_src.texture_size)
    MDBox1.add_widget(bl)
    return mdcrd


os.environ["KIVY_VIDEO"] = "ffpyplayer"
Cache.register('kv.image', timeout=100)


class FocusBehaviorLbl(HoverBehavior, ButtonBehavior):

    focus_behavior = BooleanProperty(True)
    """
	Using focus when hovering over a widget.
	:attr:`focus_behavior` is a :class:`~kivy.properties.BooleanProperty`
	and defaults to `False`.
	"""

    focus_color = ColorProperty(None)
    blur = NumericProperty(8)
    """
	The color of the widget when the mouse enters the bbox of the widget.
	:attr:`focus_color` is a :class:`~kivy.properties.ColorProperty`
	and defaults to `None`.
	"""

    unfocus_color = ColorProperty(None)
    """
	The color of the widget when the mouse exits the bbox widget.
	:attr:`unfocus_color` is a :class:`~kivy.properties.ColorProperty`
	and defaults to `None`.
	"""

    def on_enter(self):
        if self.focus_behavior:
            dialo_type = True
            main_widget = self.parent
            self.mwi = main_widget
            main_widget.radius = [30, 30, 30, 30]
            main_widget.effects = [InvertEffect()]
            dialog = MDDialog(
                title=f"[font=SF Display Regular][color=000000]{self.title}[/color][/font]",
                md_bg_color=(1, 1, 1, 1),
                text=f"[font=SF Display Regular][color=000000]{self.text_main}[/color][/font]",)
            if dialo_type:
                dialog.open()

    def on_leave(self):
        if self.focus_behavior:
            main_widget = self.parent
            main_widget.effects = []
            main_widget.color = [1, 1, 1, 1]

        """Called when the mouse exit the widget."""


class FocusBehavior(HoverBehavior, ButtonBehavior):

    focus_behavior = BooleanProperty(True)
    always_release = BooleanProperty(True)
    """
	Using focus when hovering over a widget.
	:attr:`focus_behavior` is a :class:`~kivy.properties.BooleanProperty`
	and defaults to `False`.
	"""

    focus_color = ColorProperty(None)
    blur = NumericProperty(8)
    """
	The color of the widget when the mouse enters the bbox of the widget.
	:attr:`focus_color` is a :class:`~kivy.properties.ColorProperty`
	and defaults to `None`.
	"""

    unfocus_color = ColorProperty(None)
    """
	The color of the widget when the mouse exits the bbox widget.
	:attr:`unfocus_color` is a :class:`~kivy.properties.ColorProperty`
	and defaults to `None`.
	"""

    def on_enter(self):
        if self.focus_behavior:
            (bl, img) = self.children
            text_poster = bl.children[0]
            text_poster.opacity = 1
            text_poster.font_name = "RobotoFlex"
            text_poster.color = (1, 1, 1, 1)
            with text_poster.canvas.before:
                Color(0.12, 0.12, 0.12, 1)
                rr = RoundedRectangle(pos=text_poster.pos, size=[
                                      0, 0], radius=[30, 30, 30, 30])
                anim = Animation(pos=text_poster.pos,
                                 size=text_poster.size, duration=0.100)
                anim.start(rr)
            #(name_poster,imdb,knps,effect) = self.children

    def on_leave(self):
        if self.focus_behavior:
            (bl, img) = self.children
            text_poster = bl.children[0]
            text_poster.opacity = 0
            with text_poster.canvas.before:
                Color(0, 1, 0, 0.0)
        """Called when the mouse exit the widget."""


class Tab(MDFloatLayout, MDTabsBase):
    pass


KV = '''
#: import ew kivy.uix.effectwidget
<ContentNavigationDrawer>:

	ScrollView:

		MDList:

			OneLineListItem:
				text: "Информация"
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "scr 1"

			OneLineListItem:
				text: "поиск"
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "scr 2"
			OneLineListItem:
				text: "Обзор жанра"
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "scr 3"


Screen:

	MDToolbar:

		id: toolbar
		pos_hint: {"top": 1}
		elevation: 10
		md_bg_color: app.theme_cls.primary_color 
		title: "MDNavigationDrawer"
		left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

	MDNavigationLayout:
		x: toolbar.height

		ScreenManager:
			id: screen_manager

			Screen:
				id: screen_1
				name: "scr 1"
				canvas:
					Color:
						rgba: (0.12, 0.12, 0.12, 1)
					Rectangle:
						pos: self.pos
						size: self.size
				BoxLayout:
					orientation: 'vertical'
					id: screen_1_b_l

					MDToolbar:
						specific_text_color: (1,1,1, 1)
						md_bg_color: (0.20, 0.20, 0.20, 1)
						round: "4dp"
						id: data_title
						title: 'Обзор'
						halign: "left"
						MDIconButton:
							icon: "refresh"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							user_font_size: "32sp"
							halign: "center"
							on_release: app.refresh()

						
						MDIconButton:
							id:home
							icon: "home"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							user_font_size: "32sp"
							halign: "center"
							on_release: app.home()

					BoxLayout:
						id: mainpage
						orientation: 'vertical'
						BoxLayout:
							id: mainpage_poster_info
							orientation: 'horizontal'
							BoxLayout:
								id: ViewMovieDesktop
								BoxLayout:
									orientation: 'vertical'

									MDLabel:
										id: title
										text: "Стражи Галактики 2"
										halign: "left"
										color: (1,1,1,1)
										font_size: "28px"
										font: "SF Display"


									MDLabel:
										id: eng_title
										text: "Guardians of the Galaxy Vol. 2"
										halign: "left"
										color: (0.55, 0.59, 0.70, 1)
										font_size: "16px"
										font: "SF Display"
									MDGridLayout:
										id: tags
										cols: 8
										spacing: dp(8)
									MDGridLayout:
										id: tags_rating
										cols: 2
										spacing: dp(8)
									EffectWidget:
										id: effect_desc
										FocLabel:
											id: description
											halign: "auto"
											color: (1,1,1,1)	
											text_size: self.width, None
											size_hint: 0.8, 0.8
											font: "SF Display"
											font_size: "14px"
											text: "ioniuigbuiog9gbuiobiugvuigiug00g"
							BoxLayout:
								AsyncImage:
									id:main_poster

									
						BoxLayout:
							id: similar_page
							BoxLayout:
								orientation: 'vertical'
								MDTabs:
									text_color_normal: (1,1,1, 1)
									background_color : (0.12, 0.12, 0.12, 1)
									indicator_color: (0.19, 0.37, 0.98, 1)
									Tab:
										title: "Похожее"
										ScrollView:
											do_scroll_y: False
											BoxLayout:
												padding: dp(8), dp(8)
												spacing: dp(8)
												id: similar_list
												orientation: 'horizontal'
												size_hint_x: None
												width: self.minimum_width
							




						

				  

			Screen:
				name: "scr 2"
				BoxLayout:
					orientation: "vertical"
					BoxLayout:
						id: box_search
						MDTextFieldRound:
							id: field_search
							size_hint: 3, None
							height: "30dp"
							icon_left: 'magnify'
							hint_text: "Введи запрос.."
							mode: "fill"
							fill_color: (0.20, 0.20, 0.20, 1)
							on_text: app.searcher()
							MDGridLayout:
								cols: 6
								id: images_for_ovix
								padding: dp(8), dp(8)
								spacing: dp(8)
								size_hint_y: None
								row_default_height: 200
								row_force_default: True
					BoxLayout:


			Screen:
				name: "scr 3"
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						specific_text_color: (1,1,1, 1)
						md_bg_color: (0.20, 0.20, 0.20, 1)
						round: "4dp"
						id: data_genre
						title: 'data_genre'
						halign: "left"
						MDIconButton:
							icon: "refresh"
							theme_text_color: "Custom"
							text_color: (1, 1, 1, 1)
							user_font_size: "32sp"
							halign: "center"
							on_release: app.refresh_list(self.parent)
					BoxLayout:
						orientation: 'horizontal'
						id: loader_for_ovix
						MDIconButton:
							id: back
							opacity: 0.0
							icon: "data/back.png"
							halign: "center"
							on_release: app.back()
						ScrollView:
							do_scroll_x: False
							MDGridLayout:
								cols: 6
								id: images_for_ovix
								padding: dp(8), dp(8)
								spacing: dp(8)
								row_default_height: 165
								row_force_default: True
								size_hint_y: None
								height: self.minimum_height
						MDIconButton:
							id: next
							opacity: 0.0
							icon: "data/next.png"
							halign: "center"
							on_release: app.next()

		MDNavigationDrawer:
			id: nav_drawer
			ContentNavigationDrawer:
				id: Navigation
				screen_manager: screen_manager
				nav_drawer: nav_drawer

'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        bldr = Builder.load_string(KV)
        LabelBase.register(name='Apex',
                           fn_regular='20051.ttf')
        LabelBase.register(name='RobotoFlex', fn_regular='21002.ttf')
        LabelBase.register(name='SF Display',
                           fn_regular="SF Display Regular.ttf")
        Clock.schedule_interval(self.update_frame, 1)
        return bldr

    def update_frame(self, *args):
        if len(self.root.ids.images_for_ovix.children) < 2:
            self.root.ids.home.disabled = True
        else:
            self.root.ids.home.disabled = False

    from kivy.uix.label import Label

    class FocLabel(Label, RectangularElevationBehavior, FocusBehaviorLbl):
        title = StringProperty('')
        text_main = StringProperty('')

    def on_start(self):
        self.worker_dd_panel_info("17")

    def refresh(self):
        pass

    def refresh_list(self, arg):
        toolbar = arg
        id_film = self.get_id_from_genre(toolbar.title.split(":")[-1])
        print(id_film)
        self.worker_dd_panel_info(id_film)

    def home(self):
        self.root.ids.Navigation.screen_manager.current = "scr 3"

    def next_p(self, instance, stop):
        self.pager += 1
        print(self.pager)

    def search_req(self, query):
        r = requests.get(f'https://api.ovix.tv/api/v2/search?page=1&q={query}', headers=Headers().generate()).json()["data"]

    def set_film(self, instance):
        sm = ScreenManager()
        ovtpl = self.get_info_from_ovix(instance.text)
        self.list_buttons_for_delete = []
        self.root.ids.data_title.title = f"{ovtpl.name}"
        self.root.ids.description.text = f"{ovtpl.description}"
        self.root.ids.image_preload.remove_widget(self.img)
        if not None == ovtpl.image:
            self.img = self.stand_img("https:" + ovtpl.image)
        else:
            self.img = self.stand_img(
                "https://www.jmlonline.com/img/no-product.png")
        self.root.ids.image_preload.add_widget(self.img)
        self.root.ids.tags.clear_widgets()
        for i in ovtpl.genres:
            self.root.ids.tags.add_widget(
                self.add_genre_buttons(i["name"], i["id"]))
        self.root.ids.Navigation.screen_manager.current = "scr 1"

    def cnv_size_pos(self, size, plus):
        size_x, size_y = size
        conv = [size_x + plus, size_y + plus]

    class Preloader(Image, MDLabel):
        frame_counter = 0
        frame_number = 100  # my example GIF had 2 frames

        def on_texture(self, instance, value):
            self.text = "Идёт поиск.."
            if self.frame_counter == self.frame_number + 1:
                self._coreimage.anim_reset(False)
            self.frame_counter += 1

    def on_focused(instance, value):
        print('User focused', instance)

    def get_kivy_image_from_bytes(self, image_bytes, file_extension):
        # Return a Kivy image set from a bytes variable
        buf = io.BytesIO(image_bytes)
        cim = CoreImage(buf, ext=file_extension)
        img = Image(texture=cim.texture, keep_data=False,
                    pos_hint={'center_x': .5, 'center_y': .5},)
        return img

    def get_kivy_image_texture(self, image_bytes, file_extension):
        # Return a Kivy image set from a bytes variable
        buf = io.BytesIO(image_bytes)
        cim = CoreImage(buf, ext=file_extension)
        return cim.texture

    from kivymd.uix.label import MDLabel
    # Example

    def stand_img(self, url):
        bimage = requests.get(url, timeout=3).content
        ext = url.split(".")[-1]
        image = self.get_kivy_image_from_bytes(bimage, ext)
        return image

    def stand_img_req(self, url):
        bimage = requests.get(url, timeout=3).content
        ext = url.split(".")[-1]
        return bimage, ext

    def stand_img_texture(self, url):
        bimage = requests.get(url, timeout=3).content
        ext = url.split(".")[-1]
        return bimage, ext

    class ButtonListItem(Button):
        data = StringProperty('')
        image = StringProperty('')
        title = StringProperty('')
        label = StringProperty('')
        pass

    class ButtonList(BoxLayout):
        pass

    class FocusWidget(AnchorLayout, RectangularElevationBehavior, FocusBehavior, op_button):
        Object = ObjectProperty()
        film_id = StringProperty('')

    def crete_info_panel_data(self, number, data, name_poster, text, num, other):
        (byte, exp) = data
        a = self.FocusWidget(
            anchor_x='center', anchor_y='center', film_id=other.id)
        a.bind(on_release=self.on_rel)
        i = self.get_kivy_image_from_bytes(byte, exp)
        a.add_widget(i)
        b = BoxLayout(orientation='horizontal')
        a.add_widget(b)

        self.name_MDLabel = MDLabel(text=name_poster,
                                    halign="center", opacity=0)
        self.name_MDLabel.size_hint = (0.8, 0.25)
        with self.name_MDLabel.canvas:
            Color(0, 1, 0, 0.0)
            Rectangle(pos=self.name_MDLabel.pos, size=self.name_MDLabel.size)
        b.add_widget(self.name_MDLabel)

        return a

    def search_req_sim(self, id):
        r = requests.get(f"https://api.ovix.tv/api/v2/flow/similar?type=movie&id={id}", headers=Headers().generate()).json()["data"]
        return r

    def on_rel(self, args):
        id_t = args.film_id
        print(id_t)
        sim_page = self.root.ids.similar_list

        r = self.get_info_from_ovix(id_t)
        genre_id = self.get_genre(id_t)
        data = self.search_req_sim(id_t)
        if data != None:
            for i in data:
                dt = sn(**i)
                image = blImage(
                    source="https:" + dt.image)
                image.object_poster = image

                sim_page.add_widget(generate_card(image, dt.name, dt.id))

        thread2 = threading.Thread(name='set_data_expt',
                                   target=self.set_data_expt,
                                   args=([r, genre_id]), daemon=False)
        thread2.start()

    def set_data_expt(self, ro):
        r, genre_id = ro
        self.root.ids.description.text = f"{r.description}"
        self.root.ids.description.title = f"{r.name}"
        self.root.ids.description.text_main = f"{r.description}"
        self.root.ids.main_poster.source = "https:" + r.image
        self.root.ids.eng_title.text = f"{r.name_original}"
        self.root.ids.title.text = f"{r.name}"
        self.root.ids.data_genre.title = f"Жанр: {genre_id}"

    def add_genre_buttons(self, label, idr):
        MDFillRound = MDFillRoundFlatButton(
            text=str(label) + f"({idr})",
            pos_hint={"center_x": .1, "center_y": .1},
            font_size=20,
            size=(100, 10),
            size_hint=(None, None),
            on_release=self.worker_dd_panel_info)
        return MDFillRound

    def set_item(self, data):
        print(data)
        ovix_titlles = sn(**data)
        print(ovix_titlles.id)
        self.root.ids.images_for_ovix.add_widget(self.crete_info_panel(
            text=ovix_titlles.id, number=num, url=ovix_titlles.image, name_poster=ovix_titlles.name))

    def get_genre(self, idr):
        print(idr)
        r = requests.get(f'https://api.ovix.tv/api/v2/films?page=1&genres[]={idr}', headers=Headers().generate()).json()["data"][0]["genres"]
        for i in r:
            genre = sn(**i)
            if idr == str(genre.id):
                return genre.name
                break

    def get_countr(self, idr):
        r = requests.get(f'https://api.ovix.tv/api/v2/films?page=1&countries[]={idr}', headers=Headers().generate()).json()["data"][0]["countries"]
        for i in r:
            genre = sn(**i)
            if idr == str(genre.id):
                return genre.name
                break

    def get_id_from_genre(self, idr):
        r = requests.get(f'https://api.ovix.tv/api/v2/films?page=1&genres={idr}', headers=Headers().generate()).json()["data"]
        for i in r:
            num = i["genres"]
            for i2 in num:
                genre = sn(**i2)
                if idr.strip() == str(genre.name).strip():
                    return genre.id
                    break

    def creating(self, ovix_titlles, tmpDict, num):
        tmpDict.append(sn(**{"id": ovix_titlles.id, "num": num, "image": self.stand_img_req(
            "https:" + ovix_titlles.image), "name": ovix_titlles.name, "rate": ovix_titlles.rate}))

    @mainthread
    def creatingPanel(self, *args):
        ovix_titlles, num, sec = args
        self.root.ids.images_for_ovix.add_widget(self.crete_info_panel_data(
            text=ovix_titlles.id, number=ovix_titlles.num, data=ovix_titlles.image, name_poster=ovix_titlles.name, num=num, other=ovix_titlles))

    def next(self):
        self.pager += 1

    def back(self):
        if self.pager > 0:
            self.pager -= 1

    def searcher(self, instance, value):
        print(value)

    def spawn_palels(self, r):
        tmpDict = []
        num = len(r)
        for i in r:
            ovix_titlles = sn(**i)
            self.creating(ovix_titlles, tmpDict, num)
        for num, i in enumerate(tmpDict):
            Clock.schedule_once(partial(self.creatingPanel, i, num), 0)
        self.root.ids["Preloadr"]._coreimage.anim_reset(False)
        self.root.ids["Preloadr"].parent.remove_widget(
            self.root.ids["Preloadr"])

    def convert_pager(self, json_conf, ide):
        for iter, i in enumerate(range(3), start=1):
            print(iter)
            r = requests.get(f'https://api.ovix.tv/api/v2/films?page={iter}&genres[]={ide}', headers=Headers().generate()).json()["data"]
            json_conf += r

    def worker_dd_panel_info(self, idr):
        self.root.ids.Navigation.screen_manager.current = "scr 3"
        self.Preloadr = self.Preloader(source="preloader.gif")
        self.root.ids["Preloadr"] = self.Preloadr
        self.root.ids.loader_for_ovix.add_widget(self.Preloadr)
        try:
            ide = idr.text.strip(")").split("(")[-1]
        except:
            ide = idr
        json_conf = []
        thread2 = threading.Thread(name='json_conf',
                                   target=self.convert_pager,
                                   args=(json_conf, ide), daemon=False)
        thread2.start()

        genre_id = self.get_genre(ide)
        self.root.ids.data_genre.title = f"Жанр: {genre_id}"
        self.root.ids.images_for_ovix.clear_widgets()
        self.spawn_palels(json_conf,)
        Clock.schedule_interval(self.on_update, 0.01)
        if json_conf == []:
            try:
                self.refresh()
            except:
                self.worker_dd_panel_info(idr)

    def on_update(self, *args):
        try:
            if not self.thread.is_alive():
                self.root.ids.back.opacity = 100
                self.root.ids.next.opacity = 100
        except:
            pass

    def get_info_from_ovix_rnd(self):
        ide = self.get_info_from_ovix_rnd_film()
        r = requests.get(f"https://api.ovix.tv/api/v2/films/{ide}", headers=Headers().generate()).json()["data"]
        ovix_tpl = sn(**r)
        return ovix_tpl

    def get_info_from_ovix(self, ide):
        print(ide)
        r = requests.get(f"https://api.ovix.tv/api/v2/films/{ide}", headers=Headers().generate()).json()["data"]
        ovix_tpl = sn(**r)
        return ovix_tpl

    def get_info_from_ovix_rnd_film(self):

        r = requests.get("https://api.ovix.tv/api/v2/collections/view/ZXelyAlngR",
                         headers=Headers().generate()).json()["data"]["movies"]
        liste = []
        for i in r:
            films = sn(**i)
            liste.append(films.id)
        print(liste)
        return choice(liste)


TestNavigationDrawer().run()
