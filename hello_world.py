from h2o_wave import main, Q, app, ui

@app('/')
async def serve(q: Q):
    q.page['card1'] = ui.form_card(
        box='1 1 2 1 2',
        items=[
            ui.text(f"Hello World!"),
        ]
    )

    await q.page.save()