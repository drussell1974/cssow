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
            id: 1,
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
            created: '2019-12-23T10:17:00',
            created_by_name: 'Dave Russell',
            number_of_learning_objective: 2,
        }
    },

    getLessonEpisodes() { 
        return [{
            id: 973,
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