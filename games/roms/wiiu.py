#!/usr/bin/python3
"""
Submodule containing Nintendo Wii U games and and sha1 sum
"""
from ..all.baseurl import WIIU as baseurl
from ..all.version import WIIU as version
from .. import GameCollection

__all__ = ["baseurl", "version", "games"]

games = GameCollection(baseurl, {
	"": {
		"ADVENTURES%20OF%20LOLO%20%5B000500001016b500%5D.7z": "40b4b01cfcb578e6fb734d0df2daa8df4f53ad12",
		"ALIEN%20CRUSH%20%5B000500001015bf00%5D.7z": "90a274e5d741c5504da9e7d4779b1e3fbf2f8694",
		"Advance%20Wars%20%5B000500001015e200%5D.7z": "63fad55b37dd211bbf502a292280b59b12a5734e",
		"Adventure%20Island%20%5B0005000010134200%5D.7z": "18cb01649142cfdae00fbdf09183b14f0d34091e",
		"Adventure%20Time%20Explore%20the%20Dungeon%20Because%20I%20Dont%20Know%20%5B0005000010144000%5D.7z": "0de8582881ef24ee3c44369b25cc3f6d0964bc59",
		"Air%20Zonk%20%5B000500001015ba00%5D.7z": "32cb678cc64ccf9ab779672b3fb4551b8ba62586",
		"Amazon%20Instant%20Video%20%5B0005000010102e00%5D.7z": "6091518f2afae271c837415fc82e207270bb5371",
		"Angry%20Birds%20Star%20Wars%20%5B0005000010149100%5D.7z": "cb308274ef44e0946fd5282dd3a81a30bcbfdf6b",
		"Angry%20Birds%20Trilogy%20%5B0005000010140000%5D.7z": "0bdf97ce7fa278644b803d6ca37dd19d04bca357",
		"Aqua%20Moto%20Racing%20Utopia%2080005000010172900%5D.7z": "1359a3a0cf47bccdbbf4015accb4d13eb0f2ed6f",
		"Assassins%20Creed%20III%20%5B000500001010F600%5D.7z": "2b458e23c8147073a110ee665f38238eeff7e5ee",
		"Assassins%20Creed%20V%20Black%20Flag%20%5B0005000010138800%5D.7z": "580fc9b7e7ac4f8e01c5b5e06e4a53174d03a5d2",
		"BASEBALL%20%5B0005000010149a00%5D.7z": "b14ed011b1055cfffc4edd5f99e71a8d58e511d9",
		"BATTLE%20CHOPPER%20%5B0005000010164400%5D.7z": "07cfe09d50823b53bdb765ec5ea0450e3bde034b",
		"BAYONETTA%202%20%5B0005000010172700%5D.7z": "2b417c953db32761826694e73cb12f59fd1c853f",
		"BAYONETTA%20%5B0005000010157F00%5D.7z": "1f791e12587f6e69566843dc77e95776e47afe69",
		"BEN%2010%20OMNIVERS%202%20%5B0005000010146600%5D.7z": "033127ac62c36ec5b46fffc06794aab52ffd06c6",
		"BEN%2010%20OMNIVERSE%20%5B0005000010111000%5D.7z": "6aa4ea6d7a9c0f7f8226f93b98491a50bfe24cab",
		"BOMBERMAN%20%2794%20%5B0005000010166e00%5D.7z": "a0e3e20fd81461c854690f69f48db03952e05c45",
		"BONK%203%20Bonk%27s%20Big%20Adventure%20%5B000500001015bc00%5D.7z": "2128d66625eff3c71182c6f44d3d9e860fbdd9ce",
		"BUBBLE%20BOBBLE%20%5B005000010150a00%5D.7z": "a1979bed6c7ab7313eec04c2ae017df44544f2cc",
		"Baila%20Latino%20%5B000500001017C200%5D.7z": "8a47853808a9d27bdfeccd11d12e9fee229beccd",
		"Barbie%20Dreamhouse%20Party%20%5B0005000010147B00%5D.7z": "19b0862b4e55e2ac4787119a783c58431b046001",
		"Batman%20%20Arkham%20Origins%20%5B0005000010136C00%5D.7z": "0473ed54b32f018cb4ca88576e098e7a65804ae3",
		"Batman%20Arkham%20City%20Armored%20Edition%20%5B000500001010AB00%5D.7z": "44ba8d69427d3be252336b2f583c3e3a82290999",
		"Beat%20the%20Beat%20Rhythm%20Paradise%20%5B00050000101B0800%5D%5BEUR%5D.7z": "4440c9d5c7d0138ce51016f3268c660634987980",
		"Bonk%27s%20Adventure%20%5B000500001015b600%5D.7z": "4a3e4bfea4afbd279df88bb22497ecc349239f16",
		"Bonk%27s%20Revenge%20%5B000500001015bb00%5D.7z": "6eb8a5eac6d0cf7cae6276905389b6650dfee9a5",
		"Breath%20of%20Fire%20II%20%5B0005000010134C00%5D.7z": "05271303ccb754b8d1fa1a4d9f0209740db87e3a",
		"CONTRA%20III%20THE%20ALIEN%20WARS%20%5B000500001012EF00%5D.7z": "3e4b9a220c4ec53b95c158b602e0abceac53744a",
		"Call%20of%20Duty%20Black%20Ops%20II%20%5B0005000010113400%5D.7z": "bcc7c8b137384595d11ff9b2800f01804143119e",
		"Call%20of%20Duty%20Ghosts%20%5B0005000010156100%5D.7z": "8f92fa565b63fccace9f2c24a684bee1dd1f82d8",
		"Captain%20Toad%20Treasure%20Tracker%20%20%5B0005000E10180700%5D.7z": "c412d0a3918323a1dd79b8705e74e44d71edc8ac",
		"Captain%20Toad%20Treasure%20Tracker%20%5B0005000010180600%5D.7z": "811ac770fa2484d4d75528af2d58ad78032b4009",
		"Cars%203%20Driven%20to%20Win%20%5B000500001020A400%5D.7z": "c2071def5c4d487c01410f76c26caf56e232c522",
		"Castlevania%20Aria%20of%20Sorrow%20%5B0005000010184000%5D.7z": "bf0734ad96de5e79727571581a8a45c797e2f47e",
		"Castlevania%20Circle%20of%20the%20Moon%20%5B000500001016f200%5D.7z": "cbb84d2659cacc3729c048aac6a07170b8848720",
		"Castlevania%20Dracula%20X%20%5B0005000010160100%5D.7z": "8a2249b94169260bf40110a34b577b22209f0659",
		"Castlevania%20Harmony%20of%20Dissonance%20%5B0005000010176200%5D.7z": "834d54a3c2a58ea8f71ea6852eba75f7d7726748",
		"Castlevania%20III%3A%20Dracula%27s%20Curse%20%5B000500001015f500%5D.7z": "0efa22ce80c07073ae38615aa2907badd24cdea5",
		"Castlevania%20%5B0005000010151500%5D.7z": "65477d96e66dac1b200066a7137c272180384483",
		"Castlevania%20%E2%85%A1%20Simon%27s%20Quest%20%5B0005000010153c00%5D.7z": "8c63a3766cfd7c374974c0253e3a849fc585b145",
		"Chasing%20Dead%20%5B000500001017e400%5D.7z": "4b73bdb00f49b61eb08c8515a773db9a0b804a7f",
		"Citizens%20of%20Earth%20%5B0005000010177200%5D.7z": "df213a62549625e955ecb05404b8cd11e8e45522",
		"Clu%20Clu%20Land%20%5B000500001014a600%5D.7z": "db66b380b25aab132fce075eb00d4cf96e2a8818",
		"Cybernator%20%5B0005000010140f00%5D.7z": "071714e8459db87fbc7cae57816fa005dc76dc51",
		"DEUS%20EX%20HUMAN%20REV.%20DIRECTORS%20CUT%20%5B000500001012B200%5D.7z": "fa2a7cb20a05120813e7c7663c0d851862b83af5",
		"DISNEY%20INFINITY%203.0%20PLAY%20WITHOUT%20LIMITS%20%5B00050000101B3D00%5D.7z": "b71400e5e16960bd8a57b69d41d25f01bd020336",
		"DONKEY%20KONG%203%20%5B000500001014a900%5D.7z": "4279e8cb796c72d90872de00d9fc3eaed47d6514",
		"DOUBLE%20DRAGON%20II%3A%20The%20Revenge%20%5B0005000010170d00%5D.7z": "36715fcbdd183ccbe6564c71ac0afa7f2ec62532",
		"Darksiders%20II%20%5B000500001010AD00%5D.7z": "a0db220e3f6857f257deeb5b87452ce4792ae0f3",
		"Darksiders%20Warmastered%20Edition%20%5B00050000101F9700%5D.7z": "f03f11ba3479c3b26ce109a3c0b17eb3373fd195",
		"Devils%20Third%20%5B0005000010177700%5D.7z": "3701d02a62332a9f5e0a6c234de0a2b173059f68",
		"Disney%20Epic%20Mickey%202%20%5B0005000010112E00%5D.7z": "a1c9477a93b0ff330961030731135d38d1163d6e",
		"Disney%20Infinity%20%5B2.0%5D%20%5B0005000010188C00%5D.7z": "6da5ab1bc8d212e88216282243743b5ddecd1921",
		"Disney%20Planes%20%5B0005000010136900%5D.7z": "40ee347fc5d33366b9b88925fd088a3a03c989c2",
		"Donkey%20Kong%20Country%202%3A%20Diddy%27s%20Kong%20Quest%20%5B000500001010A300%5D.7z": "5300dd5bc50d757d00c995d3f1162bc8868cc474",
		"Donkey%20Kong%20Country%203%3A%20Dixie%20Kong%27s%20Double%20Trouble%20%5B000500001017d000%5D.7z": "991cfda6c5c3ba68229878404507aca9ecd9bcd0",
		"Donkey%20Kong%20Country%20Returns%20%5B000500001019D000%5D%5BEUR%5D.7z": "da6d1406a9f78c2725c66fc0b343186763959d35",
		"Donkey%20Kong%20Country%20Tropical%20Freeze%20%5B0005000010138300%5D.7z": "3a0b72f67b4c2f1123415a59ccd2bba5566598af",
		"Donkey%20Kong%20Country%20%5B0005000010109600%5D.7z": "a56077b0d029fe22b27849ab923bbf8a91a018c3",
		"Double%20Dragon%20%5B0005000010153800%5D.7z": "7d6143faf35e6f0b41462aa1af488d28f03c8cd9",
		"Dr.%20Luigi%20%5B0005000010152a00%5D.7z": "618c8088c870536b5bfa4a51dfe2395a4ad995cd",
		"Dr.%20MARIO%20%5B0005000010153200%5D.7z": "43fa64c96738309613e7f8799ead82f22fef7f9d",
		"ESPN%20Sports%20Connection%20%5B0005000E1010B400%5D%20%5BUPDATE%20v33%5D.7z": "c167dcc90d159646108b1ce038a3875df585671c",
		"EarthBound%20Beginnings%20%5B0005000010133200%5D.7z": "59b528b352b644f9f944cffdb544adc080903bd0",
		"EarthBound%20%5B0005000010133500%5D.7z": "190d78d90e95458475c822ed15bc152e0c61de46",
		"ExciteBots%3A%20Trick%20Racing%20%5B00050000101b2600%5D.7z": "459dc023120733e9ee698e6e8bb77086515c90c9",
		"Exile%E2%80%99s%20End%20%5B00050000101ff200%5D.7z": "1188c6ef1bea828a9eab4db11fae1d149f520271",
		"F-ZERO%20MAXIMUM%20VELOCITY%20%5B0005000010156800%5D.7z": "8afa881c8e825d2fa3072ca9312e07e9c0516bc8",
		"F-Zero%20%5B0005000010119B00%5D.7z": "dfa56424fbee5e513469bbe9f7c6fe2382385289",
		"F-Zero%3A%20GP%20Legend%20%5B0005000010182b00%5D.7z": "55f6715ff3303ab57aad0418b888b8641839b0aa",
		"FAST%20Racing%20NEO%20%5B000500001012F000%5D.7z": "51716daee13527f20242afe9f1b1496c9855e3ab",
		"FAST%20Racing%20NEO%20%5B0005000C1012F000%5D%20%5BDLC%5D.7z": "2d68865f09be779ba838a2953440ab2e49137509",
		"FIFA%2013%20%5B000500001010EE00%5D.7z": "35375fdb1088cd6ecf53d61b9a1ac8a34a11f2ff",
		"Family%20Party%2030%20Great%20Games%20Obstacle%20Arcade%20%5B000500001010F300%5D.7z": "5fb41b1c399e1568455508ef4f2409fe60c97980",
		"Final%20Fight%202%20%5B0005000010137B00%5D.7z": "6be56bb1a11ca805364e4294eee81f9fbfbb8e4c",
		"Final%20Fight%203%20%5B0005000010141B00%5D.7z": "20d656a720ccc9fb6ce75f3129b6d8effdc7c859",
		"Final%20Fight%20%5B0005000010130800%5D.7z": "70818f171fe5bc461b109e967145246a1d9e155f",
		"Final%20Soldier%20%5B000500001015c300%5D.7z": "551296338713440f10a102217ee1406e4d03c9b3",
		"Fire%20Emblem%20%5B0005000010173d00%5D.7z": "99638628cd1770e6cf1cea2f5c362a7c84c6727f",
		"Fire%20Emblem%3A%20The%20Sacred%20Stones%20%5B000500001017fd00%5D.7z": "cd7eeb98e7f297d7949061a74a483e0bbb43fbcb",
		"GAME%20%26amp%3B%20WARIO%20%5B0005000010128900%5D.7z": "e2444047ce79fed945f06a35a95df9da9799e8f0",
		"GRADIUS%20%5B000500001011AE00%5D.7z": "207db9af97f23a9893ec9c4faf632832928e1c77",
		"Galaga%20%5B000500001012e400%5D.7z": "0036800b700e5877f9cab221f1ead9502452c7d9",
		"Game%20Party%20Champions%20%5B000500001010E400%5D.7z": "8f56c17a9a023ef9db165ad7378d6ee457fdbb92",
		"Game%20Party%20Champions%20%5B000500001010FF00%5D.7z": "ad50eb00b296d3667d8d4fec1a2d189ed1d3a7d7",
		"Gargoyle%27s%20Quest%20II%3A%20The%20Demon%20Darkness%20%5B000500001016c300%5D.7z": "de555c4e7974e0852adaf5e824d1ef6e64e305e9",
		"Ghosts%27n%20Goblins%20%5B0005000010134500%5D.7z": "4d47ce4a73ade20a288d540a7712b16beb9a45c4",
		"Giana%20Sisters%20Twisted%20Dreams%20%5B000500001014CB00%5D.7z": "2dcd53f53cc06a2e05b4c4e1609f0a9ef0a8752c",
		"Golden%20Sun%20%5B000500001015d900%5D.7z": "2f9702ba141e661ed3ac9b96cbf2845d10b143d9",
		"Harvest%20Moon%20%5B0005000010137700%5D.7z": "da1027af6f3716608cab4ec2ed15cf557cf66a90",
		"Hello%20Kitty%20Kruisers%20%5B0005000010147E00%5D.7z": "6c291ca8bacbc8058ef23457baf473e1b6b71a9c",
		"Hello%20Kitty%20Kruisers%20%5B0005000010177000%5D.7z": "81577275a0b670240dd5f5ba35e3918e8f3f3637",
		"Hot%20Wheels%E2%84%A2%20World%E2%80%99s%20Best%20Driver%20%5B0005000010145100%5D.7z": "d31026fb4b61c2341ee17c52edbad4591991092d",
		"Hyrule%20Warriors%20%5B000500001017D900%5D.7z": "189aa206b3bf3828b59d7fa62436b87a7a08535b",
		"IMAGEFIGHT%20%5B0005000010163e00%5D.7z": "204ee2abf8ff233f37fed5c1bf548ed2fa12e371",
		"Ice%20Hockey%20%5B0005000010150600%5D.7z": "60477342ceea553f114541cbb3322e42c1c06cac",
		"Injustice%20Gods%20Among%20Us%20%5B0005000010111A00%5D.7z": "97b3db4ad6927f823a58c89ae3a9363a07ad5ba7",
		"JUST%20DANCE%202019%20%5B0005000010217000%5D.7z": "9b98417e67ae5a9450b96a5f0b528480725c6af3",
		"Just%20Dance%C2%AE%20Kids%202014%20%5B0005000010145B00%5D.7z": "d193b8c5674c8596744799c561a7d2ee83a5c317",
		"Kid%20Icarus%20%5B000500001012FE00%5D.7z": "6622caa0213e3313a3488921907135f055784092",
		"Kirby%20%26amp%3B%20The%20AMAZING%20MIRROR%20%5B000500001015df00%5D.7z": "4666c4bfcfbc0f2455843a8c896007194efc00d6",
		"Kirby%20and%20the%20Rainbow%20Curse%20%5B00050000101ABC00%5D.7z": "d9657e5f2ab04d222ecc220d980378eb3f20488d",
		"Kirby%20and%20the%20Rainbow%20Paintbrush%20%5B00050000101B5100%5D.7z": "abbd2f6eaafcdba04716a4db79212e6ffaffed6d",
		"Kirby%27s%20Dream%20Course%20%5B0005000010119E00%5D.7z": "b6c0f5e321f9b4a07ec0aa4b4b1c1f3b1b5b845a",
		"Kung%20Fu%20Panda%20Showdown%20of%20Legendary%20Legends%20%5B0005000C101A6500%5D%20%5BDLC%5D.7z": "2de86a9ec30c6d8c228d8f62ff00dfbf253d6440",
		"Kung%20Fu%20Panda%20Showdown%20of%20Legendary%20Legends%20%5B0005000E101A6500%5D%20%5BUPDATE%20v16%5D.7z": "63ccf89b7a83f3d28ee13c57bd29c47f7f0e0b32",
		"Kung-Fu%20Heroes%20%5B0005000010161300%5D.7z": "1d9124c6008cb1d7da8129c06125bb39d95314aa",
		"LEGEND%20OF%20HERO%20TONMA%20%5B0005000010163800%5D.7z": "bebf102cdff3dc1f082e69d2bbfc64c8252a0de0",
		"LEGO%20Jurassic%20World%20%5B00050000101A5C00%5D.7z": "a04b7315ef6d7034fab524a4e960f564773ec0d8",
		"LORDS%20OF%20THUNDER%20%5B0005000010167c00%5D.7z": "a13f227fb3d63566d757bfb218c45a8554bfb008",
		"Legend%20of%20Kay%20Anniversary%20%5B0005000010193300%5D.7z": "0e6e82a8d3a4772de424d5ba422819e8b147144d",
		"Legend%20of%20Kay%20Anniversary%20%5B0005000010193400%5D.7z": "3e2a79b2c4a74951d67773f5c71d8d4cbe2b0419",
		"Lost%20in%20Shadow%20%5B00050000101B7D00%5D%5BUSA%5D.7z": "6e4270b7197b7f6ed1c3dee68f45f56bf5c6f863",
		"MARIO%20KART%207%20%28EUR%29%20%5BWUP%5D.7z": "9bed0802e6c56d349301c1c32cfcef129825995f",
		"MARIO%20KART%208%20%5B000500001010EC00%5D.7z": "ef0ba2671011de0305fc3eb3eba62de2363438df",
		"MARIO%20KART%208%20%5B000500001010ED00%5D.7z": "f2c215669e3f1c9c385ab8979d85d884c9220b66",
		"MARIO%20KART%208%20%5B0005000C1010EC00%5D%20%5BDLC%5D.7z": "6015fa9f6d7ac983dcd1d281e0d3babc64a370f6",
		"MARIO%20KART%208%20%5B0005000C1010ED00%5D%20%5BDLC%5D.7z": "7cbd10212d0b06a8b102eba6fb74ad75890ea1b5",
		"MARIO%20KART%208%20%5B0005000E1010EC00%5D%20%5BUPDATE%20v64%5D.7z": "8ab4b34c346d552943661943ebe795947a6db47a",
		"MARIO%20KART%208%20%5B0005000E1010EC00%5D%20%5BUPDATE%5D.7z": "39628ec5e23b724473d2e6c61e689bb8132ecb4a",
		"MARIOKART%208%20Campaign%20Soft%20%5B0005000010183a00%5D.7z": "1692fc3c3cf47e7a3ee6d4c5d3afb4ae89080ec5",
		"MEGA%20MAN%202%20%5B0005000010114900%5D.7z": "2b56a8fccf2c011addead59902d6ecf8f834e096",
		"MEGA%20MAN%203%20%5B000500001012A000%5D.7z": "68c031fb9438883eaf262ec9840ff61d7f2f2b03",
		"MEGA%20MAN%204%20%5B000500001012E800%5D.7z": "ea334e4db1c2d24d81580d8de0585c8ad7bbffbf",
		"MEGA%20MAN%205%20%5B000500001016c000%5D.7z": "2f8b9fb02fc0525b3dd809ba841b3ac27570d236",
		"MEGA%20MAN%206%20%5B0005000010160d00%5D.7z": "5d7b3cf0033ff225e7c7fa66aebdbf66a35a34fb",
		"MEGA%20MAN%207%20%5B0005000010174000%5D.7z": "bc6b1624c74bb60399609723c95c17a31a3c6b86",
		"MEGA%20MAN%20X3%20%5B0005000010175300%5D.7z": "4722d6424059875da87ce67b884d1b17ff720ce0",
		"MEGA%20MAN%20%5B0005000010114600%5D.7z": "420981f2e3d56928adf7dcae02d31c9f04389f67",
		"METROID%20Other%20M%20%5B000500001019E100%5D.7z": "94b43d86a2efe229bf4e1bc0e9a2ca175b232938",
		"MIGHTY%20BOMB%20JACK%20%5B0005000010158b00%5D.7z": "4085dc153217c495ca0927d5749348bbf4880962",
		"Mach%20Rider%20%5B0005000010160900%5D.7z": "e7d85b35f5e7c74ebb7daf98d5d0323c77eb6f1d",
		"Mario%20%26amp%3B%20Luigi%3A%20Superstar%20Saga%20%5B0005000010157500%5D.7z": "a9d0f1f08c78c2a2d3dbeb2aca77b751e7e403a6",
		"Mario%20Kart%3A%20Super%20Circuit%20%5B000500001017d200%5D.7z": "330775faeb2d20ac63907e72e55430ebff48094d",
		"Mario%20Party%2010%20%5B0005000010162D00%5D.7z": "bc06230ce395362868b55438f908ecb3acf314e2",
		"Mario%20Party%2010%20%5B0005000010162E00%5D.7z": "af3a5b49c88597df0f4e6ea3c4b20fc6a4935a6c",
		"Mario%20Pinball%20Land%20%5B0005000010174f00%5D.7z": "aa220a2e4fc490e20e4c7a283ff45c3cf3c31c8f",
		"Mario%20Power%20Tennis%20%5B0005000010169b00%5D.7z": "c8f726021807f562b32da18a9cf79e1499a8d6f7",
		"Mario%20Sports%20MIX%20%5B00050000101B1B00%5D.7z": "e94b1df0dc4254edca691722d2fbfb35429bf327",
		"Mario%20Sports%20Mix%20%5B00050000101B1A00%5D%5BUSA%5D.7z": "a869b80433dcf0adaed14f4c1f2aa8dd95b32733",
		"Mario%20Tennis%20Ultra%20Smash%20%5B00050000101A3600%5D.7z": "098ea3c50600ecbc1fbff3c809f2a0b7c09d357a",
		"Mario%20and%20Sonic%20at%20the%20Sochi%202014%20Olympic%20Winter%20Games%20%5B000500001010c800%5D.7z": "719cb1e21772567da42cdfa597bbf366a23d4f01",
		"Mario%20vs.%20Donkey%20Kong%20Tipping%20Stars%20%5B0005000010178E00%5D.7z": "2a48ea8bcd353ac5dddd9a5f0b89ff83c264db65",
		"Mario%20vs.%20Donkey%20Kong%20Tipping%20Stars%20%5B0005000010179200%5D.7z": "47674cb927fd90870a17dd0acb75f6b0639c5c42",
		"Mario%20vs.%20Donkey%20Kong%20%5B000500001015dc00%5D.7z": "99ad3ac7dd2669b87d2bb11fb30584b204e3788c",
		"Mass%20Effect%203%20Special%20Edition%20%5B000500001010F500%5D.7z": "24698bac97137e6c7d09c9679cc364debd115842",
		"Master%20Reboot%20%5B000500001016e800%5D.7z": "89a0fdfea00995217f8345ff3fee27310cb183da",
		"Mega%20Man%20X%20%5B0005000010130E00%5D.7z": "55c7c9529db7dbccc40e579cbb36699eaf4981cd",
		"Mega%20Man%20X2%20%5B0005000010141800%5D.7z": "dc3d95f92c94f4f9a03144f80396d7d5ebd92033",
		"Metroid%20Fusion%20%5B0005000010157100%5D.7z": "e7fff0fd847680fc5f29a785a20d69f1a35f7f83",
		"Metroid%20Fusion%20%5B0005000010157200%5D.7z": "1e2b06957a66118dcf322e54ac5815957fa868ee",
		"Metroid%20%5B000500001012f500%5D.7z": "981bcb75288003c0d31f2d80d55cb57f05dd9368",
		"Metroid%3A%20Zero%20Mission%20%5B000500001016fa00%5D.7z": "0772d6e1e5fe6a28a151dcff33e7e4cbdd76d487",
		"Mighty%20No.%209%20%5B0005000C101C9600%5D%20%5BDLC%5D.7z": "f7fc22f3387cf1942290cb7425603ecc86f16475",
		"Mighty%20No.%209%20%5B0005000E101C9600%5D%20%5BUPDATE%20v16%5D.7z": "beb4e26e3551cb1c421045f18ad80da29c90cda3",
		"Minecraft%20Story%20Mode%20%5B00050000101E0100%5D.7z": "ec2f0ac70b2c6d358b4003872f7db5688c4fb73f",
		"Minecraft%20Wii%20U%20Edition%20%5B00050000101D9D00%5D.7z": "0753e320024cd93df3bcebf3860062f34e63ae1f",
		"Monster%20High%20New%20Ghoul%20in%20School%20%5B00050000101C8D00%5D.7z": "58d0a54092baf5e5b297952cd4507ef100f8236d",
		"NES%20Open%20Tournament%20Golf%20%5B0005000010152f00%5D.7z": "c152ad351de24f68f8c26de6e2753e393cc94578",
		"NES%20REMIX%20%5B0005000010146100%5D.7z": "96178a5358cd2f9768ffd9155bee358fd5a70e4a",
		"NES%20REMIX%20%5BUPDATE%5D%20%5B0005000E10146100%5D.7z": "4e017edb41deafa6d0732ca91f92dc994e2d7a3a",
		"NEUTOPIA%20II%20%5B000500001015c000%5D.7z": "043d4f0c5f34edf7099597a2bbe39c443a1076d8",
		"NEUTOPIA%20%5B000500001015b900%5D.7z": "99874206e63c97cf737ef7149fd51544de452088",
		"NINJA%20GAIDEN%20%5B0005000010158800%5D.7z": "bb4ddc4c6d534baaf209af68bc5f512d40909472",
		"NINJA%20SPIRIT%20%5B0005000010163b00%5D.7z": "9618aabea12f03ed0f2c7ab2241e7ee0ee91136c",
		"Need%20for%20Speed%20Most%20Wanted%20U%20%5B0005000010128400%5D.7z": "b51247b0168d6271b08a70152c319430cbeeb157",
		"New%20Adventure%20Island%20%5B000500001015b700%5D.7z": "b6d383f815b79b51c8600856cbbf1af662b646f8",
		"New%20SUPER%20MARIO%20BROS.%20U%20%2B%20New%20SUPER%20LUIGI%20U%20%5B000500001014B700%5D.7z": "e43f7b766b7c8a8bd5d3cb5281c75b5787d7e564",
		"New%20SUPER%20MARIO%20BROS.%20U%20%2B%20New%20SUPER%20LUIGI%20U%20%5B000500001014B800%5D.7z": "a2670f110986d04870831604f839f798defb042b",
		"New%20SUPER%20MARIO%20BROS.%20U%20%5B0005000010101D00%5D.7z": "cc3923b912ba5367baf9e4a44a7110712de2f3f4",
		"New%20SUPER%20MARIO%20BROS.%20U%20%5B0005000010101E00%5D.7z": "ff5c96635900de1ca2a44a72f1807aeb4e0d9f60",
		"Nintendo%20Land%20%5B0005000010102000%5D.7z": "29cc63fdca9547ec96c3145a59266b7467b0e96b",
		"PAC-LAND%20%5B000500001016b900%5D.7z": "2a0814b6fc62782a8bad5e10ed9e58c77dafacb8",
		"PAPER%20MARIO%20Color%20Splash%20%20%5B000500001f600B00%5D.7z": "c6431b6fd85a1bd8b98e7e9fb23c73647dce2ad9",
		"PENGUIN%20ADVENTURE%20%5B0005000010168200%5D.7z": "b6487d3a2121eb87ba740489c8fdcaf916cc864a",
		"PINBALL%20%5B000500001014a000%5D.7z": "ff7eab9a977f8215cdd8e795197755a316fa4d98",
		"Pandora%27s%20Tower%20%5B00050000101B1400%5D%5BEUR%5D.7z": "aeb4e9d623a09ceacb7db2fce52b57e074d41745",
		"Pandora%27s%20Tower%20%5B00050000101B1400%5D%5BEUR%5D_1.7z": "aeb4e9d623a09ceacb7db2fce52b57e074d41745",
		"Pilotwings%20%5B0005000010130500%5D.7z": "932026994c550a26434cb30e49ad2eee81c6ede2",
		"Pinball%20Arcade%20%28EUR%29%20%5BWUP%5D.7z": "b0b71f17af94b0a8609abe9b77e4895e0d353efa",
		"Pinball%20Breakout%20%5B0005000010206c00%5D.7z": "f3401b66d5434e325e78c815bb531b628744d4fa",
		"Project%20Zero%20Maiden%20of%20Black%20Water%20%5B00050000101D3F00%5D.7z": "a763e71260d4fea8671baeefc3ba3b6a0d6e418d",
		"Punch-Out%21%21%20%5B0005000010108C00%5D.7z": "69a1480358fef153dd8ced473c7dc044c6f8f830",
		"R-TYPE%20%5B000500001016a500%5D.7z": "673656c92627e21af9618fe4765845c62901b64b",
		"RESIDENT%20EVIL%20REVELATIONS%20%5B000500001012CF00%5D.7z": "530690aa92a2a269dcd17e088fe224d46c5e92ba",
		"RESIDENT%20EVIL%20REVELATIONS%20%5B0005000C1012CF00%5D%20%5BDLC%5D.7z": "ce3fb3a10a64457986ff169ca7faaee49dfca5d8",
		"RUBIKS%20CUBE%20%5B0005000010156400%5D.7z": "9b77205accadf6c3ac82616569c25dcc2bb31c10",
		"Rayman%20Legends%20Challenges%20App%20%5B0005000010139500%5D.7z": "939618566f272be9c0ee45ba5e4df5d966e39075",
		"Renegade%20%5B0005000010153500%5D.7z": "8d8a4e02f61f0a40ebed6a3140834e76807fd9ab",
		"Rhythm%20Heaven%20Fever%20%5B00050000101B0700%5D%5BUSA%5D.7z": "8fa72c376108a8f52315843e164004ff74726944",
		"Rock%20%27N%20Racing%20Off%20Road%20DX%20%5B00050000101D8D00%5D.7z": "c1422d6149c5d16e5a7d0f18ff1b3fa11386866b",
		"Rock%20%27N%20Racing%20Off%20Road%20DX%20%5B00050000101d9600%5D.7z": "7628fe287c896095431adc00745c0c205212e1d5",
		"Rock%20%27N%20Racing%20Off%20Road%20%5B00050000101dd300%5D.7z": "dcad69995e85ea95602a03aafd6c935e7669361f",
		"Romance%20of%20The%203%20Kingdoms%20%E2%85%A3%20Wall%20of%20Fire%20%5B0005000010136000%5D.7z": "8578465fc8702b272ac289e4078dacad5e20c5d2",
		"SONIC%20LOST%20WORLD%20%5B0005000010128F00%5D.7z": "1ea19cfa16ee0c9a558198408c61835e13b18bc6",
		"SONIC%20LOST%20WORLD%20%5B0005000C10128F00%5D%20%5BDLC%5D.7z": "32dd54f2d2b787c85727015a57e536966a4fc6d7",
		"SUPER%20MARIO%203D%20WORLD%20%5B0005000010145C00%5D.7z": "27019b93d868d4e547577ee900ec5b8983b00ed9",
		"SUPER%20MARIO%203D%20WORLD%20%5B0005000010145D00%5D.7z": "d4e682172c441694446dea0fb6fd940dd01c234a",
		"Secret%20Files%20Tunguska%20%5B00050000101C5B00%5D.7z": "0f2b176b0276b5ce0c00ef665d81f92f981f37f8",
		"Shiftlings%20%5B00050000101A7F00%5D.7z": "79da2a296d4208acb08335e2d30b0a049abf2f22",
		"Shockman%20%5B000500001015c100%5D.7z": "e42cdab6a245e6e9f2e26635d7ff07e0f893f011",
		"Sin%20%26amp%3B%20Punishment%20Successor%20of%20the%20Skies%20%5B00050000101B0B00%5D%5BEUR%5D.7z": "802643bb9de4bdb5d363da4eab63d93abe9291e5",
		"Soccer%20%5B0005000010160600%5D.7z": "db8cf575ca884f19b533833a0878e37f58f95a82",
		"Solomon%27s%20Key%20%5B0005000010129D00%5D.7z": "973eb4110ca3c4a44ab4291c04d3c4c73e21de18",
		"Sonic%20%26amp%3B%20All-Stars%20Racing%20Transformed%20%5B000500001010B300%5D.7z": "2c5eb652dd21bc637b9d33e275bb7bdff7c1cdb5",
		"Sonic%20%26amp%3B%20All-Stars%20Racing%20Transformed%20%5B0005000E1010B300%5D%20%5BUPDATE%20v48%5D.7z": "f3f90c3434390bf0f6c5711334ab5b4fea93d238",
		"Sonic%20Boom%20Rise%20of%20Lyric%20%5B0005000010175B00%5D.7z": "c5839fc48a22164e16c3b443f2fcfb819442f28c",
		"Sonic%20Boom%20Rise%20of%20Lyric%20%5B0005000010177800%5D.7z": "08fd0aa8f1b8f06b726d1708a36afe8dc6b3688a",
		"SpongeBob%20SquarePants%20Planktons%20Robotic%20Revenge%20%5B0005000010146900%5D.7z": "5e4806dd99ea75633e276632b98b1ac762805a10",
		"Star%20Fox%20Guard%20%5B00050000101BEC00%5D.7z": "5e393812fcf78a204b965dc044a4fc2823617884",
		"Star%20Fox%20Zero%20The%20Battle%20Begins%20%2B%20Training%20%5B0005000010201B00%5D.7z": "8daa6797ea124709bd33652d9203815cb851acc9",
		"Star%20Fox%20Zero%20%5B00050000101B0400%5D.7z": "57b373c78189193a3513437c6108fe5cce61ae35",
		"Star%20Fox%20Zero%20%5B00050000101B0500%5D.7z": "14daa1d4998a9220721d74add49d592898657273",
		"Street%20Fighter%20Alpha%202%20%5B000500001016c600%5D.7z": "afa35127d653a66ecad84d12743ea7d3a9bcc027",
		"Street%20Fighter%20II%20Turbo%20Hyper%20Fighting%20%5B000500001012AD00%5D.7z": "cacdd1eb19ea0dc28b48d7be8803c587aaf6e174",
		"Street%20Fighter%20%E2%85%A1%20The%20World%20Warrior%20%5B0005000010115100%5D.7z": "9ac59423aeaaf6fc53bea7ccb345473b2476b38f",
		"Super%20C%20%5B0005000010158f00%5D.7z": "a64f70dd87c937934731061d9e6594758135d054",
		"Super%20Castlevania%20%E2%85%A3%20%5B0005000010130B00%5D.7z": "5a9032fb2fe0ad69b4c21fa0f4c72ddddfabefb2",
		"Super%20Dodge%20Ball%20%5B0005000010151200%5D.7z": "0ac02f47fa2607093b7888cc51c3a48133fac3f2",
		"Super%20Ghoulsn%20Ghost%20%5B000500001011A100%5D.7z": "469557f551293424f8268aa1fc69fdfff1b89247",
		"Super%20Mario%20Advance%204%3A%20Super%20Mario%20Bros.%203%20%5B0005000010169e00%5D.7z": "4eab6325895175d2cfa4b202f35da6c5d3a6150f",
		"Super%20Mario%20Advance%20%5B0005000010173700%5D.7z": "f239d12286d7b897b82ea79eddcf07ae7e8ed616",
		"Super%20Mario%20Bros.%202%20%5B0005000010108600%5D.7z": "427a4318d66e750dfd0368e2d15133a9f0815670",
		"Super%20Mario%20Bros.%203%20%5B0005000010107100%5D.7z": "d05e97fc6c9aefc2f1297a20856e7ae9820e097c",
		"Super%20Mario%20Bros.%20The%20Lost%20Levels%20%5B000500001012F800%5D.7z": "d97c28f92983f54f71cd817357f0ef19ada33e29",
		"Super%20Mario%20Kart%20%5B000500001010AA00%5D.7z": "171d172162c7c3db6bbb559dd544435fc3b3c4f7",
		"Super%20Mario%20Maker%20%5B000500001018DC00%5D.7z": "571d2cc195475b2a2f3686d981e7b83375d3fd75",
		"Super%20Mario%20RPG%3A%20Legend%20of%20the%20Seven%20Stars%20%5B0005000010109200%5D.7z": "b13a3fe86c80e2ffe669a24b09b5466fde2943f1",
		"Super%20Mario%20RPG%3A%20Legend%20of%20the%20Seven%20Stars%20%5B0005000010109300%5D.7z": "ea92933b04cf17c9825241b0d77e0b302dc059c1",
		"Super%20Mario%20World%20%5B0005000010109000%5D.7z": "8a4a988a8b5089843b1c99741d7d0ad282acb237",
		"Super%20Mario%20World%3A%20Super%20Mario%20Advance%202%20%5B000500001016f600%5D.7z": "2a27330f7e8d5de9196370bc976400a509ecff42",
		"Super%20Metroid%20%5B000500001010A700%5D.7z": "d5bb457b1f1b0f18504ffed5626c67ee5318e78e",
		"Super%20Paper%20Mario%20%5B00050000101BD200%5D%5BEUR%5D.7z": "a75850037f68eac41a3a33fc0daebb786ee9be49",
		"Super%20Smash%20Bros.%20for%20Wii%20U%20%5B0005000010144F00%5D.7z": "966cf10ae0f5e17548d7b38e52542fd006b4822e",
		"Super%20Street%20Fighter%20%E2%85%A1%20The%20New%20Challengers%5B%20000500001011A500%5D.7z": "adb351bd3c4b7f16a6b5cde3badfeca497c53720",
		"Super%20Toy%20Cars%20%5B000500001016d500%5D.7z": "51025730088f739db4759d44d43c0bece41382c7",
		"TANK%21%20TANK%21%20TANK%21%20%28DL%29%20%5B0005000010133800%5D.7z": "55e57643cfe2f788c6e747c9f97f756bd4e6522b",
		"TENNIS%20%5B0005000010149d00%5D.7z": "17c0b4a2e0c6bd0db3e780f3406dcf2f11da5371",
		"THE%20CROODS%20%5B0005000010112000%5D.7z": "482a630053ab3695bba6e5fb8b057e8f0e087e03",
		"THE%20LEGEND%20OF%20ZELDA%20The%20Wind%20Waker%20HD%20%5B0005000010143500%5D.7z": "b45b8004ff1c74d43da158c54dadbaa4baed18d4",
		"THE%20LEGEND%20OF%20ZELDA%20Twilight%20Princess%20HD%20%5B000500001019E500%5D.7z": "00b0ab0b23969fa788249e7cfbd6b0fb107d4923",
		"TRANSFORMERS%20PRIME%20%5B000500001010B500%5D.7z": "3bba50c4261edee741f40ad6c50fe900986c6adf",
		"The%20Amazing%20Spider-Man%202%20%5B0005000010128300%5D.7z": "81c04f61ecb9edbc896cf447726edbd01d046641",
		"The%20Fall%20%5B00050000101b2800%5D.7z": "6bef3353847705eb0183aeeb4eade259569bf1e2",
		"The%20Legend%20of%20The%20Mystical%20Ninja%20%5B0005000010114D00%5D.7z": "f81a548d37b26df3a8292b8fdc69e15ee792803b",
		"The%20Legend%20of%20Zelda%20Breath%20of%20the%20Wild%20%5B00050000101C9500%5D.7z": "322db3fb02493fd8a6c4fb5873cf43e428afeb7c",
		"The%20Legend%20of%20Zelda%20Hyrule%20Historia%20%5B000500001014CA00%5D.7z": "b4335a27af8048c054b3c621093094ac06ac594f",
		"The%20Legend%20of%20Zelda%20Skyward%20Sword%20%5B00050000101B1000%5D%5BUSA%5D.7z": "12b753d6e4cb1096e04adedff600f25144353342",
		"The%20Legend%20of%20Zelda%20Skyward%20Sword%20%5B00050000101B1100%5D%5BEUR%5D.7z": "edd56309e61c5426a4012e958b284e0d45337198",
		"The%20Legend%20of%20Zelda%20%5B000500001012FB00%5D.7z": "9094f35ca952a3523fb869d0e792daea0e1a9e6d",
		"The%20Legend%20of%20Zelda%3A%20A%20Link%20to%20the%20Past%20%5B0005000010109A00%5D.7z": "92fd390813a582053bb75918f048c61ac2f95b8e",
		"The%20Legend%20of%20Zelda%3A%20The%20Minish%20Cap%20%5B000500001015e400%5D.7z": "a98e08a18979dd1d46080a6438b4e14a13ebab19",
		"The%20Legend%20of%20Zelda%3A%20The%20Minish%20Cap%20%5B000500001015e500%5D.7z": "562ec4f261cd1ae8d508746f2dc4c46c140bf5a5",
		"Turbo%20Super%20Stunt%20Squad%20%5B0005000010133900%5D.7z": "6e84c6954321e0aa86142192d4b172bbee455c26",
		"Ufouria%3A%20THE%20SAGA%20%5B0005000010171300%5D.7z": "410090e8f2a160746f17b9c70265cbbb754068f6",
		"Uncharted%20Waters%3A%20New%20Horizons%20%5B0005000010141300%5D.7z": "e688adb0f1b4f9f42e79d4f0af2f23f12035291f",
		"Uplay%20%5B000500001011b700%5D.7z": "788a62c2057bcfe280a01991c39e6ecf05a7d900",
		"Urban%20Champion%20%5B000500001014a300%5D.7z": "1917ac51e228b85b61c44b7aaa123ab15d50012e",
		"VIGILANTE%20%5B0005000010163500%5D.7z": "1673ed5e2c22e385737d95f7df4b2fc93ff051e0",
		"WARRIORS%20OROCHI%203%20Hyper%28NA%29%20%5B0005000010110200%5D.7z": "02fdd0f1faa8cd40a19464a2de0c5af4f680f426",
		"WATCH_DOGS%20%5B0005000010140500%5D.7z": "2a5958d9b3abc4640094331acdcd34e2e271c886",
		"WATCH_DOGS%20%5B0005000010142000%5D.7z": "61178bb5f3bd2b802bea03775c5208390ecfc0d1",
		"WATCH_DOGS%20%5BDLC%5D%20%5B0005000c10140500%5D.7z": "bd2ebc3f4ce7a832848127a43c91de49799897af",
		"Wario%20Land%204%20%5B000500001016a100%5D.7z": "7063b43d0abda3df469b5a2b4e27179a891dba58",
		"Wario%20Land%20Shake%20It%20%5B00050000101BDF00%5D%5BUSA%5D.7z": "56c3fffe31dd02c95450d74e9462fe9b969f39f1",
		"Wario%20Ware%2C%20Inc.%20Minigame%20Mania%20%5B0005000010156f00%5D.7z": "8b40ec072858b2348d889aab0b88aa154d32366c",
		"Wario%27s%20Woods%20%5B0005000010150900%5D.7z": "b43a6fbe79ff59d15c0f21e27fd6c379f76f41ec",
		"Wii%20Fit%20U%20Quick%20Check%20%5B0005000010132600%5D.7z": "1b04be83737d67fbdd8a7a1602ce0bf0bdbd2145",
		"Wii%20Fit%20U%20%5B0005000010102300%5D.7z": "8575a95753895ddc02b9d3195f866514114780e3",
		"Wrecking%20Crew%20%5B000500001012E000%5D.7z": "eeea2ff480a6e3b69ed34e473873776ee3d7807f",
		"Yoshi%20Touch%20%26amp%3B%20Go%5B0005000010179e00%5D.7z": "cd26b53994c6a316c27c333f55347067dd9a4a62",
		"Yoshi%27s%20Island%3A%20Super%20Mario%20Advance%203%20%5B005000010156b00%5D.7z": "9f5ad0cf2b947e2386c4f991006f267ab4da88cf",
		"Zelda%20II%20-%20The%20Adventure%20of%20Link%20%5B0005000010130100%5D.7z": "80e306330aedf284ef3c36ae0ae7f7ca822b02f0",
		"Zombeer%20%5B000500001019ea00%5D.7z": "8627d59bf6279313838d22cacd2d95519e85c905",
		"ZombiU%20%20%5B005000E1010DD00%5D%20%5BUPDATE%5D.7z": "5dcecf85cd02d36e273c728f03f90efc14f7f1a5",
		"ZombiU%20%5B000500001010DD00%5D.7z": "3a000ecea997d523cb802178b6d6ab985f361cc7",
		"Zombie%20Defense%20%5B00050000101a1800%5D.7z": "46bec3f529c712563aa491bb4c06c829e5a7db75",
		"wii-u-romset-iso-dump-eu-us_archive.torrent": "a3d48cb13d38ef4db86a1fe71f4e968632b1d4f8",
		"wii-u-romset-iso-dump-eu-us_files.xml": "",
		"wii-u-romset-iso-dump-eu-us_meta.sqlite": "0b0b9fb54f11b0fcb84fb6ce3586870528f951ae",
		"wii-u-romset-iso-dump-eu-us_meta.xml": "ce1735b15859e14af1dbd6a70a4866a2857f55af" }
})