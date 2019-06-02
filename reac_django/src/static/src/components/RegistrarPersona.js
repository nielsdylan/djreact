import React, {Component} from 'react';

class RegistrarPersona extends Component {
    render(){
        return (
            <div className="App">
                  <label>DNI</label>
                  <input type="text" name="dni" />
                  <label>Apellido Paterno</label>
                  <input type="text" name="apellidoPaterno" />
                  <label>Apellido Materno</label>
                  <input type="text" name="apellidoMaterno" />
                  <label>Nombres</label>
                  <input type="text" name="nombres" />
                  <label>Direccion</label>
                  <input type="text" name="direccion" />
                  <label>Telefono</label>
                  <input type="text" name="telefono" />
              
            </div>
          );
        }

    }
  
export default RegistrarPersona;