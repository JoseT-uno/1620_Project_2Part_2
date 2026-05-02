from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtWidgets import *
from wgui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWid.setCurrentWidget(self.page_main)

        self.ms_start_btn.clicked.connect(lambda: self.ms_start_button())

        #Choose Screen Section
        self.choose_srcn_ff_btn.clicked.connect(lambda: self.display_ff_scrn())
        self.choose_srcn_sf_btn.clicked.connect(lambda: self.display_scrn_sf())
        self.choose_srcn_tf_btn.clicked.connect(lambda: self.display_scrn_tf())
        self.choose_scrn_home_btn.clicked.connect(lambda: self.display_home_scrn())

        #First Floor Section
        self.ff_return_btn.clicked.connect(lambda: self.ms_start_button())
        self.ff_choose_btn.clicked.connect(lambda: self.ff_handle_dropdown_option())
        self.ff_map_btn.clicked.connect(lambda: self.ff_display_map(confirm=False))
        self.ms_uno_label.setStyleSheet("background-color: rgb(179, 179, 179);")
        self.map_scrn_return_btn.clicked.connect(lambda: self.display_ff_scrn())

        self.ff_continue_btn.clicked.connect(lambda: self.ff_handle_output_desire_floor())

        self.pg_image_btn.clicked.connect(lambda: self.display_ff_scrn())
        self.ff_specific_room_drpdwn.setVisible(False)
        self.ff_continue_btn.setVisible(False)

        #FF Map Section
        self.ff_map_confirm_btn.clicked.connect(lambda: self.ff_display_map(confirm =True))
        ff_mapcheckboxes = [self.ff_map_rm_164_CB, self.ff_map_rm_161_CB, self.ff_map_rm_160_CB,
            self.ff_map_rm_157_CB, self.ff_map_rm_155_CB, self.ff_map_rm_153_CB,
            self.ff_map_fish_bowl_CB, self.ff_map_rm_IST_Office_CB, self.ff_map_rm_Eng_Office_CB,
            self.ff_map_rm_Dean_Office_CB, self.ff_map_rm_Cafe_CB, self.ff_map_additional_lounge_CB,
            self.ff_map_triangle_lounge_CB, self.ff_map_Cafe_lounge_CB
                ]
        for ff_checkbox in ff_mapcheckboxes:
            ff_checkbox.toggled.connect(self.ff_map_display_selection)
        self.map_scrn_display_btn.clicked.connect(lambda: self.stackedWid.setCurrentWidget(self.from_map_to_image_display()))

    def ms_start_button(self):
        self.stackedWid.setCurrentWidget(self.page_choose)

    def display_home_scrn(self):
        self.stackedWid.setCurrentWidget(self.page_main)

    def display_ff_scrn(self):
        self.stackedWid.setCurrentWidget(self.page_ff)
    def ff_returnscreen(self):
        self.stackedWid.setCurrentWidget(self.page_main)

    def ff_handle_dropdown_option(self):
        available_options = ["Classroom", "Bathroom", "Lounges", "Office/Faculty", "Cafe"]
        chosen_option = self.ff_choose_room_drpdwn.currentText().strip() # added strip
        if chosen_option in available_options:
            QMessageBox.information(self, "Info", f"You have selected {chosen_option}.")
            self.ff_specific_room_drpdwn.setVisible(True)
            self.ff_continue_btn.setVisible(True)
            room_specific = {"Classroom": ["153" ,"155", "157", "160", "161", "164"],
                             "Bathroom": ["Main Entrance", "Near Cafe"],
                             "Office/Faculty": ["IS&T Department", "Office of Dean"],
                             "Lounges": ["Fish Bowl"],
                             "Cafe": ["Cafe"]
                             }
            self.ff_specific_room_drpdwn.clear()
            specific_room = room_specific.get(chosen_option, [])
            self.ff_specific_room_drpdwn.addItems(specific_room)

        else:
            self.ff_specific_room_drpdwn.setVisible(False)
            self.ff_continue_btn.setVisible(False)
            QMessageBox.information(self, "Error", f"You have selected nothing.")

    def ff_handle_output_desire_floor(self):
        selected_room = self.ff_specific_room_drpdwn.currentText()


        pathway_photo = None
        if selected_room == "153":
            photo_path = r"R153.JPG"
        elif selected_room == "157":
            photo_path = r"R157.JPG"
        #Ofiice/Faculty Section
        elif selected_room == "IS&T Department":
            pathway_photo = r"FF To Office.jpeg"
            photo_path = r"FF IST Office.JPG"
        elif selected_room == "Office of Dean":
            pathway_photo = r"FF To Office.jpeg"
            photo_path = r"FF Office of Dean.JPG"

        elif selected_room == "Cafe":
            photo_path = r"FF Cafe.JPG"

        #Lounge Section
        elif selected_room == "Fish Bowl":
            photo_path = r"FF Fish Bowl.JPG"
        else:
            photo_path = r"placeholder.png"
        path = QPixmap(pathway_photo)
        pixmap = QPixmap(photo_path)


        if not pixmap.isNull():
            transform = QTransform()
            transform.rotate(90)
            rotated_pixmap = pixmap.transformed(transform)
            rotate_pathway = path.transformed(transform)

            self.ff_page_image_pathway.setPixmap(rotate_pathway)
            self.ff_page_image_pathway.setScaledContents(True)
            self.pg_image_output.setPixmap(rotated_pixmap)
            self.pg_image_output.setScaledContents(True)

        else:
            print(f"File not found: {photo_path}")
        self.stackedWid.setCurrentWidget(self.page_image)

    def ff_display_map(self, confirm=False):
        self.stackedWid.setCurrentWidget(self.page_ff_map)

        ff_checkboxes = [
            self.ff_map_rm_164_CB, self.ff_map_rm_161_CB, self.ff_map_rm_160_CB,
            self.ff_map_rm_157_CB, self.ff_map_rm_155_CB, self.ff_map_rm_153_CB,
            self.ff_map_fish_bowl_CB, self.ff_map_rm_IST_Office_CB, self.ff_map_rm_Eng_Office_CB,
            self.ff_map_rm_Dean_Office_CB, self.ff_map_rm_Cafe_CB, self.ff_map_additional_lounge_CB,
            self.ff_map_triangle_lounge_CB, self.ff_map_Cafe_lounge_CB
        ]
        if not confirm:
            for cb in ff_checkboxes:
                cb.setVisible(True)
            return
        for cb in ff_checkboxes:
            cb.setVisible(False)


        grouped_cbs = {
            "Classroom": [
                self.ff_map_rm_164_CB, self.ff_map_rm_161_CB,
                self.ff_map_rm_160_CB, self.ff_map_rm_157_CB,
                self.ff_map_rm_155_CB, self.ff_map_rm_153_CB
            ],
            "Lounges": [self.ff_map_fish_bowl_CB, self.ff_map_additional_lounge_CB,
                        self.ff_map_Cafe_lounge_CB, self.ff_map_triangle_lounge_CB],
            "Cafe": [self.ff_map_rm_Cafe_CB],
            "Bathroom": [],
            "Office/Faculty": [self.ff_map_rm_IST_Office_CB, self.ff_map_rm_Eng_Office_CB, self.ff_map_rm_Dean_Office_CB]
        }


        if self.ff_map_drpdwn.currentIndex() == 0:
            QMessageBox.information(self, "Info", f"Select valid opt.")
            for cb in ff_checkboxes:
                cb.setVisible(True)
                cb.setChecked(False)
            return


        options = self.ff_map_drpdwn.currentText().strip()
        QMessageBox.information(self, "Recognized Option", f"The option you chose is {options}")
        if options in grouped_cbs:
            for cbs in grouped_cbs[options]:
                cbs.setVisible(True)
        else:
            QMessageBox.information(self, "Info", f"Invalid selection: {options}")

    def ff_map_display_selection(self, checked):
        if checked:
            cbs = self.sender()
            room_names = {
                self.ff_map_rm_153_CB: "153",
                self.ff_map_rm_155_CB: "155",
                self.ff_map_rm_157_CB: "157",
                self.ff_map_rm_160_CB: "160",
                self.ff_map_rm_161_CB: "161",
                self.ff_map_rm_164_CB: "164",
                self.ff_map_fish_bowl_CB: "Fish Bowl",
                self.ff_map_rm_IST_Office_CB: "IS&T Office",
                self.ff_map_rm_Eng_Office_CB: "Engineering Office",
                self.ff_map_rm_Dean_Office_CB: "Dean's Office",
                self.ff_map_rm_Cafe_CB: "Cafe",
                self.ff_map_additional_lounge_CB: "Additional Lounge",
                self.ff_map_triangle_lounge_CB: "Middle Lounge",
                self.ff_map_Cafe_lounge_CB: "Cafe Lounge",
            }
            room_chosen = room_names.get(cbs, "Unknown Room")
            QMessageBox.information(self, "Location Selected", f"You have selected : {room_chosen}")

    def from_map_to_image_display(self):
        self.stackedWid.setCurrentWidget(self.page_image)

    def display_scrn_sf(self):
        display_message = "You pressed 2nd Floor button"
        QMessageBox.information(self, "Info", display_message)

    def display_scrn_tf(self):
        display_message = "You pressed 3rd Floor button"
        QMessageBox.information(self, "Info", display_message)
