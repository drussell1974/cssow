const ApiReactService = {
    
    getSchemesOfWork(reactComponent) {
        fetch("http://127.0.0.1:8000/api/schemeofwork")
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                reactComponent.setState({
                    SchemesOfWork: data.schemesofwork, 
                    hasError: false,
                });
            },  
            (error) => {
                reactComponent.setState({
                    SchemesOfWork: {},
                    hasError: true,
                });
            }
        )
    },

    getLessons(reactComponent, schemeOfWorkId) {
        let uri = `http://127.0.0.1:8000/api/schemeofwork/${schemeOfWorkId}/lessons`

        fetch(uri)
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                reactComponent.setState({
                    Lessons: data.lessons, 
                    hasError: false,
                });
            },  
            (error) => {
                reactComponent.setState({
                    Lessons: {},
                    hasError: true,
                });
            }
        )
    },
    
    getLesson(reactComponent, schemeOfWorkId, learningObjectiveId) {
        /*let uri = `http://127.0.0.1:8000/api/schemeofwork/${schemeOfWorkId}/lessons/${learningObjectiveId}`

        fetch(uri)
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                reactComponent.setState({
                    Lesson: data.lesson, 
                    hasError: false,
                });
            },  
            (error) => {
                reactComponent.setState({
                    Lesson: {},
                    hasError: true,
                });
            }
        )*/
        var lesson = {
            id: 64,
            title: "CPU architecture",
            order_of_delivery_id: 1,
            scheme_of_work_id: 127,
            scheme_of_work_name: "GCSE Computer Science 9-1",
            topic_id: 4,
            topic_name: "Hardware and architecture",
            parent_topic_id: 0,
            parent_topic_name: "Computing",
            related_topic_ids: [],
            key_stage_id: 4,
            key_stage_name: "",
            year_id: 10,
            year_name: "Yr10",
            key_words: "Von neumann architecture,Central Processing Unit (CPU),Fetch Decode Execute (FDE),Control Unit (CU),Buses,Current Instruction Register (CIR),Data bus,Control bus,Address bus,Program Counter (PC),Arithemtic Logic Unit (ALU),Accumulator (ACC),Memory Data Register (MDR),Memory Address Register (MAR),System Clock",
            other_key_words: [ ],
            summary: "Von Neumann architecture and the CPU",
            pathway_objective_ids: [ ],
            pathway_ks123_ids: [ ],
            created: "2019-01-15T08:32:00",
            created_by_id: 1,
            created_by_name: "Mr Russell",
            published: 1,
            orig_id: 0,
            key_words_from_learning_objectives: "Memory, Current Instruction Register (CIR), Memory Address Register (MAR), Memory Data Register (MDR), Memory Data Register (MDR), Random Access Memory (RAM),Central Processing Unit (CPU), Registers, Memory, Random Access Memory (RAM),,Current Instruction Register (CIR), Program Counter (PC), Central Processing Unit (CPU), Registers, Memory, Arithemtic Logic Unit (ALU), Accumulator (ACC), Memory Address Register (MAR), Accumulator (ACC),,,,Central Processing Unit (CPU), Buses, Control bus, Address bus, Data bus, Cache, Multi-core,Multi-core, Central Processing Unit (CPU), Chip MultiProcessor (CMP),Interrupt code, Operating System (OS)",
            number_of_learning_objective: 12,
            learning_objectives: [],
            number_of_resource: 2
        }
        reactComponent.setState({
            Lesson: lesson,
            hasError: true,
        });
    }
}

export default ApiReactService;
