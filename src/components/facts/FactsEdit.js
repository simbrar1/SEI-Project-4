import React from 'react'
import axios from 'axios'
import FactsForm from './FactsForm'
import Auth from '../../lib/Auth'

class FactsEdit extends React.Component {
  constructor() {
    super()

    this.state = { data: {} }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/facts/${this.props.match.params.id}`)
      .then(res => this.setState({ data: res.data }))
      .catch(err => console.log(err.response))
  }

  handleChange({ target: { name, value}}) {
    const data = {...this.state.data, [name]: value}
    this.setState({ data }, () => console.log(this.state.data))
  }

  handleSubmit(e){
    e.preventDefault()

    axios.put(`/api/facts/${this.props.match.params.id}`, this.state.data,{
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
      .then(() => this.props.history.push(`/facts/${this.props.match.params.id}`))
      .catch(err => console.log(err.response))
  }


  render() {
    return(
      <section className="section">
        <div className="main">
          <FactsForm
            data={this.state.data}
            handleChange={this.handleChange}
            handleSubmit={this.handleSubmit}
          />
        </div>
      </section>
    )
  }
}


export default FactsEdit
