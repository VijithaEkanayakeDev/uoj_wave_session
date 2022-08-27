from h2o_wave import main, Q, app, ui


@app('/')
async def serve(q: Q):
    q.page['card1'] = ui.form_card(box='1 1 2 2', items=[
        ui.text(content='Hello World!!'),
        ui.textbox(name='name', label="Name"),
        ui.button(name='submit', label="Submit"),
    ])
    if q.args.submit:
        q.page['card2'] = ui.form_card(box='1 3 2 2', items=[
            ui.text(content=f'Name sent by the user is: {q.args.name}'),
        ])
    await q.page.save()
