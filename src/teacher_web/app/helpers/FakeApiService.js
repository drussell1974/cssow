const FakeApiService = {
    
    getSchemeOfWork() {
        return {
            id: 1,
            name: 'GCSE Computer Science',
            key_stage_name: 'Key Stage 4',
            created_by_name: 'Dave Russell',
            is_recent: true,
            get_ui_created: function(){
                return "22nd December 2019";
            },
        };
    },

    getSchemesOfWork() {
        return [{
            id: 1,
            name: 'Computing',
            key_stage_name: 'Key Stage 3',
            created_by_name: 'Dave Russell',
            is_recent: false,
            get_ui_created: function(){
                return "22nd December 2019";
            },
        },
        {
            id: 1,
            name: 'GCSE Computer Science',
            key_stage_name: 'Key Stage 4',
            created_by_name: 'Dave Russell',
            is_recent: true,
            get_ui_created: function(){
                return "22nd November 2019";
            },
        },
        {
            id: 3,
            name: 'A-Level Computer Science',
            key_stage_name: 'Key Stage 5',
            created_by_name: 'Dave Russell',
            is_recent: false,
            get_ui_created: function(){
                return "1st July 2019";
            },
        }];
    }
}

export default FakeApiService;