const getState = ({ getStore, getActions, setStore}) => {
    return {
        store: {
            apiURL: 'https://5000-marellanorero-apiweb-4cmtq5xfwke.ws-us62.gitpod.io',
            contacts: null,
            contact: null
        },
        actions: {
            getContacts: async (url) =>{
                try {
                    const response = await fetch(url+'/api/contacts');
                    if (!response.ok) throw new Error("Error al consultar contactos");
                    const data = await response.json();

                    setStore({
                        contacts: data
                    })
                } catch (error) {
                    console.log(error)
                }
            },
            getContactById: async (url, id) =>{
                try {
                    const response = await fetch(url+'/api/contacts'+id);
                    if (!response.ok) throw new Error("Error al consultar el contacto");
                    const data = await response.json();

                    setStore({
                        contact: data
                    })
                } catch (error) {
                    console.log(error)
                }
            },
            setContact: (contact) => {
                setStore({
                    contact: contact
                })
            },
        }
    }
}

export default getState;