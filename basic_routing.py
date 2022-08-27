from h2o_wave import main, Q, app, ui, handle_on, on


@app('/')
async def serve(q: Q):
    if not q.client.initialized:
        await init_client(q)

    await handle_on(q)
    await q.page.save()


async def init_client(q):
    q.page['card1'] = ui.form_card(box='1 1 2 2', items=[
        ui.text(content='Hello World!!'),
        ui.textbox(name='name', label="Name"),
        ui.button(name='submit', label="Submit"),
    ])
    q.client.initialized = True


@on()
async def submit(q: Q):
    q.page['card2'] = ui.form_card(box='1 3 2 2', items=[
        ui.text(content=f'Name sent by the user is: {q.args.name}'),
    ])
