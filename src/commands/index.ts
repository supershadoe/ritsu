`use strict`;

import { ApplicationCommandOptionType, ApplicationCommandType } from "discord-api-types/v10";
import { DAYS_OF_WEEK } from "../utils";

const GuildOnlySlashCommand = {
    dm_permission: false,
    type: ApplicationCommandType.ChatInput
}

export const PUBCHEM = {
    ...GuildOnlySlashCommand,
    name: "pubchem",
    description: "Fetch the details of a compound from PubChem",
    options: [
        {
            name: "compound_name",
            description:
              "The name of the compound " +
              "/ Try to use IUPAC Name for accurate result",
            type: ApplicationCommandOptionType.String,
            required: true
        }
    ]
}

export const FANDOM = {
    ...GuildOnlySlashCommand,
    name: "fandom",
    description: "Search for any article from any fandom",
    options: [
        {
            name: "search_term",
            description: "Term to search for",
            type: ApplicationCommandOptionType.String,
            required: true
        },
        {
            name: "fandom_name",
            description: "Fandom site to search in",
            type: ApplicationCommandOptionType.String,
            required: true
        }
    ]
};

export const WIKIPEDIA = {
    ...GuildOnlySlashCommand,
    name: "wikipedia",
    description: "Search for any article from wikipedia",
    options: [
        {
            name: "search_term",
            description: "Term to search for",
            type: ApplicationCommandOptionType.String,
            required: true
        }
    ]
}

export const SUBSPLEASE = {
    ...GuildOnlySlashCommand,
    name: "subsplease",
    description: "Commands to access Subsplease API",
    options: [
        {
            name: "schedule",
            description: "Shows release schedule of Subsplease",
            type: ApplicationCommandOptionType.Subcommand,
            options: [
                {
                    name: "day_of_week",
                    description: "Day of week to fetch schedule for",
                    type: ApplicationCommandOptionType.String,
                    choices: DAYS_OF_WEEK.map((d) => ({ name: d, value: d })),
                    required: false
                }
            ]
        }
    ]
}
// TODO default: DAYS_OF_WEEK[(new Date()).getDay()],
// TODO create a KV Namespace with all command ids for both testing and stable bot.