const FakeApiService = {
    
    getSchemeOfWork() {
        return {
            id: 1,
            name: 'GCSE Computer Science',
            key_stage_name: 'Key Stage 4',
            created_by_name: 'Dave Russell',
            is_recent: true,
            created: '21st December 2019',
        };
    },

    getSchemesOfWork() {
        return [{
            id: 1,
            name: 'Computing',
            key_stage_name: 'Key Stage 3',
            created_by_name: 'Dave Russell',
            is_recent: false,
            created: '22nd December 2019',
        },
        {
            id: 2,
            name: 'GCSE Computer Science',
            key_stage_name: 'Key Stage 4',
            created_by_name: 'Dave Russell',
            is_recent: true,
            created: '22nd November 2019',
        },
        {
            id: 3,
            name: 'A-Level Computer Science',
            key_stage_name: 'Key Stage 5',
            created_by_name: 'Dave Russell',
            is_recent: false,
            created: '1st July 2019',
        }];
    },
    
    getLessonEpisode() { 
        return {
            id: 1,
            scheme_of_work_id: 99,
            order_of_delivery_id: 1,
            title: 'Components of the CPU',
            summary: 'Program Counter, ALU, Cache',
            year_name: 'Year 10',
            topic_name: 'Hardware',
            key_words: 'Program Counter (PC),Arithmetic Logic Unit (ALU)',
            key_words_from_learning_objectives: 'Program Counter (PC),Arithmetic Logic Unit (ALU),Cache',
            created: '2019-12-23T10:17:00',
            created_by_name: 'Dave Russell',
            number_of_learning_objective: 2,
            learning_objectives: [
                {
                    id: 462,
                    description: "Describe the function of the Arithmetic Logic Unit (ALU)",
                    notes: " ",
                    scheme_of_work_name: "",
                    solo_taxonomy_id: 2,
                    solo_taxonomy_name: "Multistructural: Describe, List (give an account or give examples of)",
                    solo_taxonomy_level: "B",
                    topic_id: 7,
                    topic_name: "CPU",
                    parent_topic_id: null,
                    parent_topic_name: [
                    8
                    ],
                    content_id: 25,
                    content_description: "characteristics of contemporary systems architectures, including processors, storage, input, output and their connectivity",
                    exam_board_id: 3,
                    exam_board_name: "OCR",
                    learning_episode_id: 131,
                    learning_episode_name: 1,
                    key_stage_id: 5,
                    key_stage_name: "KS5",
                    parent_id: null,
                    key_words: "Arithemtic Logic Unit (ALU), Program Counter (PC)",
                    group_name: "",
                    is_key_objective: true,
                    created: "2019-01-15T13:28:33",
                    created_by_id: 1,
                    created_by_name: "Mr Russell",
                    published: 1
                },
                {
                    id: 463,
                    description: "Describe how the Control Unit manages the other CPU components",
                    notes: " ",
                    scheme_of_work_name: "",
                    solo_taxonomy_id: 2,
                    solo_taxonomy_name: "Multistructural: Describe, List (give an account or give examples of)",
                    solo_taxonomy_level: "B",
                    topic_id: 7,
                    topic_name: "CPU",
                    parent_topic_id: null,
                    parent_topic_name: [
                    8
                    ],
                    content_id: 25,
                    content_description: "characteristics of contemporary systems architectures, including processors, storage, input, output and their connectivity",
                    exam_board_id: 3,
                    exam_board_name: "OCR",
                    learning_episode_id: 131,
                    learning_episode_name: 1,
                    key_stage_id: 5,
                    key_stage_name: "KS5",
                    parent_id: null,
                    key_words: "Control Unit (CU)",
                    group_name: "",
                    is_key_objective: true,
                    created: "2019-01-15T13:30:12",
                    created_by_id: 1,
                    created_by_name: "Mr Russell",
                    published: 1
                },
                {
                    id: 464,
                    description: "Explain how the different registers are used to store data and carry data over the buses",
                    notes: " ",
                    scheme_of_work_name: "",
                    solo_taxonomy_id: 3,
                    solo_taxonomy_name: "Relational: Explain, Compare, Justify and Give Reasons (evaluate or assess)",
                    solo_taxonomy_level: "C",
                    topic_id: 8,
                    topic_name: "Memory",
                    parent_topic_id: null,
                    parent_topic_name: [
                    8
                    ],
                    content_id: 25,
                    content_description: "characteristics of contemporary systems architectures, including processors, storage, input, output and their connectivity",
                    exam_board_id: 3,
                    exam_board_name: "OCR",
                    learning_episode_id: 131,
                    learning_episode_name: 1,
                    key_stage_id: 5,
                    key_stage_name: "KS5",
                    parent_id: null,
                    key_words: "Program Counter (PC),Address bus,Data bus,Control bus,Memory Data Register (MDR),Accumulator (ACC),Memory Address Register (MAR)",
                    group_name: "",
                    is_key_objective: true,
                    created: "2019-01-15T13:34:44",
                    created_by_id: 1,
                    created_by_name: "Mr Russell",
                    published: 1
                },
                {
                    id: 465,
                    description: "Explain the steps carried out by the Fetch Decode Execute cycle",
                    notes: " ",
                    scheme_of_work_name: "",
                    solo_taxonomy_id: 3,
                    solo_taxonomy_name: "Relational: Explain, Compare, Justify and Give Reasons (evaluate or assess)",
                    solo_taxonomy_level: "C",
                    topic_id: 7,
                    topic_name: "CPU",
                    parent_topic_id: null,
                    parent_topic_name: [
                    8
                    ],
                    content_id: 25,
                    content_description: "characteristics of contemporary systems architectures, including processors, storage, input, output and their connectivity",
                    exam_board_id: 3,
                    exam_board_name: "OCR",
                    learning_episode_id: 131,
                    learning_episode_name: 1,
                    key_stage_id: 5,
                    key_stage_name: "KS5",
                    parent_id: null,
                    key_words: "Fetch Decode Execute (FDE),Decode unit,Opcode,Operand",
                    group_name: "",
                    is_key_objective: true,
                    created: "2019-01-15T13:37:32",
                    created_by_id: 1,
                    created_by_name: "Mr Russell",
                    published: 1
                },
                {
                    id: 466,
                    description: "Give the reasons why a branch in the program may occur",
                    notes: " ",
                    scheme_of_work_name: "",
                    solo_taxonomy_id: 2,
                    solo_taxonomy_name: "Multistructural: Describe, List (give an account or give examples of)",
                    solo_taxonomy_level: "B",
                    topic_id: 7,
                    topic_name: "CPU",
                    parent_topic_id: null,
                    parent_topic_name: [
                    8
                    ],
                    content_id: 25,
                    content_description: "characteristics of contemporary systems architectures, including processors, storage, input, output and their connectivity",
                    exam_board_id: 3,
                    exam_board_name: "OCR",
                    learning_episode_id: 131,
                    learning_episode_name: 1,
                    key_stage_id: 5,
                    key_stage_name: "KS5",
                    parent_id: null,
                    key_words: "Program branch",
                    group_name: "",
                    is_key_objective: true,
                    created: "2019-01-15T13:43:30",
                    created_by_id: 1,
                    created_by_name: "Mr Russell",
                    published: 1
                },
            ],
        }
    },

    getLessonEpisodes() { 
        return [{
            id: 396,
            scheme_of_work_id: 99,
            order_of_delivery_id: 1,
            title: 'CPU Architecture',
            summary: 'Von Neumann architecture and the CPU',
            year_name: 'Yr10',
            topic_name: 'Hardware and architecture',
            created: '2019-12-23T10:17:00',
            created_by_name: 'Dave Russell',
            number_of_learning_objective: 12,
        },{
            id: 397,
            scheme_of_work_id: 99,
            order_of_delivery_id: 2,
            title: 'Memory',
            summary: 'Random Access Memory (RAM), virtual memory and cache',
            year_name: 'Yr10',
            topic_name: 'Hardware and architecture',
            created: '2019-12-23T10:17:00',
            created_by_name: 'Dave Russell',
            number_of_learning_objective: 2,
        },{
            id: 398,
            scheme_of_work_id: 99,
            order_of_delivery_id: 3,
            title: 'Computer architecture',
            summary: 'Types of computer including embedded systems',
            year_name: 'Yr10',
            topic_name: 'Hardware and architecture',
            created: '2019-12-23T10:17:00',
            created_by_name: 'Dave Russell',
            number_of_learning_objective: 6,
        },{
            id: 399,
            scheme_of_work_id: 99,
            order_of_delivery_id: 1,
            title: 'Intro to Networks',
            summary: 'Types of networks and transmission media',
            year_name: 'Yr10',
            topic_name: 'Communication and networks',
            created: '2019-12-23T10:17:00',
            created_by_name: 'Dave Russell',
            number_of_learning_objective: 5,
        }]
    }
}

export default FakeApiService;