from h2o_wave import site, ui

page = site['/']

page["card3"] = ui.form_card(box='1 6 2 2', items=[
    ui.text(content='From script'),
])
page.save()