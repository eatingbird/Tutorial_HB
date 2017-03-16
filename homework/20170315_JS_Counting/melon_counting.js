"use strict";

var melons_to_add = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
                     'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas',
                     'Christmas', 'Christmas', 'Watermelon', 'Sharlyn', 'Xigua',
                     'Cantaloupe', 'Christmas', 'Watermelon', 'Christmas',
                     'Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
                     'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen',
                     'Horned Melon', 'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn',
                     'Horned Melon', 'Sharlyn', 'Cantaloupe', 'Christmas',
                     'Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 'Xigua',
                     'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
                     'Watermelon', 'Santa Claus', 'Casaba'];


function count_melons(melon_list){
    // """Takes in a list, and returns a dictionary with melon counts."""

    var melon_counts = {};

    for (var i=0; i<melon_list.length; i++){
        var melon = melon_list[i];
        if (melon in melon_counts){
            melon_counts[melon] = melon_counts[melon] + 1;
        }
        else{
            melon_counts[melon] = 1;
        }
    }
    return melon_counts;
}

console.log(count_melons(melons_to_add));