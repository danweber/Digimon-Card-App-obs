export const replacements: Array<[RegExp, string]> = [
  [/ACE/g, 'ace'],
  [/\[All Turns]/g, 'all_turns'],
  [/＜Alliance＞/g, 'alliance'],
  [/＜Armor Purge＞/g, 'armor_purge'],
  [/\[At End of Opponent's Turn]/g, 'at_end_of_opponents_turn'],
  [/＜Barrier＞/g, 'barrier'],
  [/＜Blast Digivolve＞/g, 'blast_digivolve'],
  [/＜Blitz＞/g, 'blitz'],
  [/＜Blocker＞/g, 'blocker'],
  [/Burst Digivolve:/g, 'burst_digivolve'],
  [/\[Breeding]/g, 'breeding'],
  [/\[Counter]/g, 'counter'],
  [/＜Decoy \[Bagra Army] traits＞/g, 'decoy_bagra_army'],
  [/＜Decoy \(Black\)＞/g, 'decoy_black'],
  [/＜Decoy \(Black\/White\)＞/g, 'decoy_black_white'],
  [/＜Decoy \(D-Brigade\)＞/g, 'decoy_d-brigade'],
  [/＜Decoy \(Bagra Army\)＞/g, 'decoy_bagra_army'],
  [/＜Decoy \(Deva\/Four Sovereigns\)＞/g, 'decoy_deva_four_sovereigns'],
  [/＜Decoy \(Red\/Black\)＞/g, 'decoy_red_black'],
  [/＜De-Digivolve＞/g, 'de-digivolve'],
  [/＜De-Digivolve 1＞/g, 'de-digivolve_1'],
  [/＜De-Digivolve 2＞/g, 'de-digivolve_2'],
  [/＜De-Digivolve 3＞/g, 'de-digivolve_3'],
  [/＜De-Digivolve 4＞/g, 'de-digivolve_4'],
  [/＜De-Digivolve1＞/g, 'de-digivolve_1'],
  [/＜De-Digivolve2＞/g, 'de-digivolve_2'],
  [/＜De-Digivolve3＞/g, 'de-digivolve_3'],
  [/＜De-Digivolve4＞/g, 'de-digivolve_4'],
  [/＜Delay＞/g, 'delay'],
  [/＜Digi-Burst ＞/g, 'digi-burst_1'],
  [/＜Digi-Burst 1＞/g, 'digi-burst_1'],
  [/＜Digi-Burst 2＞/g, 'digi-burst_2'],
  [/＜Digi-Burst 3＞/g, 'digi-burst_3'],
  [/＜Digi-Burst 4＞/g, 'digi-burst_4'],
  [/＜Digi-Burst up to 4＞/g, 'digi-burst_up_to_4'],
  [/＜Digisorption -1＞/g, 'digisorption_-1'],
  [/＜Digisorption -2＞/g, 'digisorption_-2'],
  [/＜Digisorption -3＞/g, 'digisorption_-3'],
  [/Digivolve:/g, 'digivolve'],
  [/\[Digivolve]/g, 'digivolve'],
  [/\[DigiXros -1]/g, 'digixros_-1'],
  [/\[DigiXros -2]/g, 'digixros_-2'],
  [/\[DigiXros -3]/g, 'digixros_-3'],
  [/\[DNA Digivolve]/g, 'dna_digivolve'],
  [/＜Draw 1＞/g, 'draw_1'],
  [/＜Draw 2＞/g, 'draw_2'],
  [/＜Draw 3＞/g, 'draw_3'],
  [/\[End of All Turns]/g, 'end_of_all_turns'],
  [/\[End of Attack]/g, 'end_of_attack'],
  [/\[End of Opponent's Turn]/g, 'end_of_opponents_turn'],
  [/\[End of Your Turn]/g, 'end_of_your_turn'],
  [/＜Evade＞/g, 'evade'],
  [/＜Fortitude＞/g, 'fortitude'],
  [/\[Hand]/g, 'hand'],
  [/\[Main]/g, 'main'],
  [/＜Mind Link＞/g, 'mind_link'],
  [/＜Jamming＞/g, 'jamming'],
  [/＜Material Save 1＞/g, 'material_save_1'],
  [/＜Material Save 2＞/g, 'material_save_2'],
  [/＜Material Save 3＞/g, 'material_save_3'],
  [/＜Material Save 4＞/g, 'material_save_4'],
  [/\[On Deletion]/g, 'on_deletion'],
  [/\[On Play]/g, 'on_play'],
  [/\[Once Per Turn]/g, 'once_per_turn'],
  [/\[Opponent's Turn]/g, 'opponents_turn'],
  [/Overflow ＜-3＞/g, 'overflow_-3'],
  [/Overflow ＜-4＞/g, 'overflow_-4'],
  [/＜Piercing＞/g, 'piercing'],
  [/＜Raid＞/g, 'raid'],
  [/＜Reboot＞/g, 'reboot'],
  [/＜Recovery \+1 \(Deck\)＞/g, 'recovery_+1deck'],
  [/＜Recovery \+2 \(Deck\)＞/g, 'recovery_+2deck'],
  [/＜Retaliation＞/g, 'retaliation'],
  [/＜Rush＞/g, 'rush'],
  [/\[Rule]/g, 'rule'],
  [/＜Save＞/g, 'save'],
  [/\[Security]/g, 'security'],
  [/＜Security Attack＞/g, 'security_attack'],
  [/＜Security Attack -1＞/g, 'security_attack_-1'],
  [/＜Security Attack \+1＞/g, 'security_attack_+1'],
  [/＜Security Attack \+2＞/g, 'security_attack_+2'],
  [/＜Security Attack -2＞/g, 'security_attack_-2'],
  [/＜Security Attack -3＞/g, 'security_attack_-_3'],
  [/\[Start of Your Main Phase]/g, 'start_of_your_main_phase'],
  [/\[Start of Your Turn]/g, 'start_of_your_turn'],
  [/\[Start of Opponent's Turn]/g, 'start_of_opponents_turn'],
  [/\[Trash]/g, 'trash'],
  [/\[Twice Per Turn]/g, 'twice_per_turn'],
  [/\[When Digivolving]/g, 'when_digivolving'],
  [/\[When Attacking]/g, 'when_attacking'],
  [/\[Your Turn]/g, 'your_turn'],
  [
    /＜Partition \(blue Lv.4 \+ green Lv.4\)＞/g,
    'partition_blue_lv.4_green_lv.4',
  ],
  [
    /＜Partition \(red Lv.4 \+ yellow Lv.4\)＞/g,
    'partition_red_lv.4_yellow_lv.4',
  ],
  [
    /＜Partition \(black Lv.4 \+ yellow Lv.4\)＞/g,
    'partition_black_lv.4_yellow_lv.4',
  ],
  [
    /＜Partition \(purple Lv.4 \+ red Lv.4\)＞/g,
    'partition_purple_lv.4_red_lv.4',
  ],
  [
    /＜Partition \(yellow Lv.4 \+ black Lv.4\)＞/g,
    'partition_yellow_lv.4_black_lv.4',
  ],
];

export const keywordTooltip: Map<string, string> = new Map<string, string>([
  ['ace', ''],
  ['all_turns', ''],
  ['alliance', ''],
  ['armor_purge', ''],
  ['at_end_of_opponents_turn', ''],
  ['barrier', ''],
  ['blast_digivolve', ''],
  ['blitz', ''],
  ['blocker', ''],
  ['burst_digivolve', ''],
  ['breeding', ''],
  ['counter', ''],
  ['decoy_bagra_army', ''],
  ['decoy_black', ''],
  ['decoy_black_white', ''],
  ['decoy_d-brigade', ''],
  ['decoy_red_black', ''],
  ['de-digivolve', ''],
  ['de-digivolve_1', ''],
  ['de-digivolve_2', ''],
  ['de-digivolve_3', ''],
  ['de-digivolve_4', ''],
  ['delay', ''],
  ['digi-burst_1', ''],
  ['digi-burst_1', ''],
  ['digi-burst_2', ''],
  ['digi-burst_3', ''],
  ['digi-burst_4', ''],
  ['digi-burst_up_to_4', ''],
  ['digisorption_-1', ''],
  ['digisorption_-2', ''],
  ['digisorption_-3', ''],
  ['digivolve', ''],
  ['digivolve', ''],
  ['digixros_-1', ''],
  ['digixros_-2', ''],
  ['digixros_-3', ''],
  ['dna_digivolve', ''],
  ['draw_1', ''],
  ['draw_2', ''],
  ['draw_3', ''],
  ['end_of_all_turns', ''],
  ['end_of_attack', ''],
  ['end_of_opponents_turn', ''],
  ['end_of_your_turn', ''],
  ['evade', ''],
  ['fortitude', ''],
  ['hand', ''],
  ['main', ''],
  ['mind_link', ''],
  ['jamming', ''],
  ['material_save_1', ''],
  ['material_save_2', ''],
  ['material_save_3', ''],
  ['material_save_4', ''],
  ['on_deletion', ''],
  ['on_play', ''],
  ['once_per_turn', ''],
  ['opponents_turn', ''],
  ['overflow_-3', ''],
  ['overflow_-4', ''],
  ['piercing', ''],
  ['raid', ''],
  ['reboot', ''],
  ['recovery_+1deck', ''],
  ['recovery_+2deck', ''],
  ['retaliation', ''],
  ['rush', ''],
  ['rule', ''],
  ['save', ''],
  ['security', ''],
  ['security_attack', ''],
  ['security_attack_-1', ''],
  ['security_attack_+1', ''],
  ['security_attack_+2', ''],
  ['security_attack_-2', ''],
  ['security_attack_-_3', ''],
  ['start_of_your_main_phase', ''],
  ['start_of_your_turn', ''],
  ['trash', ''],
  ['twice_per_turn', ''],
  ['when_digivolving', ''],
  ['when_attacking', ''],
  ['your_turn', ''],
]);
