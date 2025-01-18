import flet as ft

def main(page:ft.Page):
    page.title = 'Counter App'
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    txt=ft.TextField(value="0",text_align ="center",width=100)


    def increase(e):
        txt.value = str(int(txt.value)+ 1)
        page.update()


    def decrease(e):
        txt.value =str(int(txt.value)-1)
        page.update()

    page.add(ft.Row([
        ft.IconButton(ft.Icons.REMOVE, on_click=decrease),
        txt,
        ft.IconButton(ft.Icons.ADD, on_click=increase),


    ],
    alignment = ft.MainAxisAlignment.CENTER
    )
    )




ft.app(main)