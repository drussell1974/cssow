const FakeApiService = {
    
    getSchemeOfWork() {
        return {
            id: 1,
            name: 'GCSE Computer Science',
            key_stage_name: 'Key Stage 3',
            created_by_name: 'Dave Russell',
            is_recent: true,
            get_ui_created: function(){
                return "22nd December 2019";
            },
        };
    },

    getSchemesOfWork() {
        return [];
    }
}

export default FakeApiService;