"""Slash commands for accessing pubchem API"""

import alluka
import hikari
import tanjun

from ritsu.handlers.pubchem import hooks
from ritsu.utils.pubchem import fetch_compound, gen_compound_embed, gen_action_row


@hooks.add_to_command
@tanjun.with_str_slash_option(
    "compound_name", "Try to use IUPAC Name for accurate results"
)
@tanjun.as_slash_command(
    "pubchem", "Fetch the details of a compound from PubChem",
    always_defer=True
)
async def cmd_pubchem(
    ctx: tanjun.abc.SlashContext,
    compound_name: str,
    client: alluka.Injected[tanjun.Client],
    action_row: hikari.api.ActionRowBuilder = (
        tanjun.cached_inject(gen_action_row)
    )
) -> None:
    """To fetch details of a compound from PubChem"""

    result = await client.injector.call_with_async_di(
        fetch_compound, compound_name
    )
    if "ritsu_error" in result:
        err: tuple = result["ritsu_error"]
        if isinstance(dict, err[1]):
            error: dict = err[1]
            embed: hikari.Embed = (
                hikari.Embed(
                    title="Error", description=f"_{error['Details'][0]}._",
                    color=0xFF0000
                )
                .add_field("Code", f"**{error['Code']}**", inline=True)
                .add_field("Message", error["Message"], inline=True)
            )
        else:
            embed: hikari.Embed = hikari.Embed(
                title="Error",
                description=f"_{0}: {1}_".format(*err),
                color=0xFF0000
            )
        await ctx.edit_initial_response(
            embed=embed,
            content=(
                "Oh no! An error has occurred while trying to fetch the "
                "required data! :fearful:\nTry again later :pensive:"
                "\n\n_Or contact the bot developer for debugging_"
            )
        )
        return

    await ctx.edit_initial_response(
        "Here's the release schedule of SubsPlease.",
        embed=gen_compound_embed(result),
        component=action_row
    )

comp_pubchem: tanjun.Component = tanjun.Component(name="comp_pubchem").load_from_scope()
comp_pubchem.make_loader()

__all__: tanjun.typing.Final[list[str]] = ['comp_pubchem']
