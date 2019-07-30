import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Auth from '../../lib/Auth'
import CommentForm from '../common/CommentForm'
import Comment from '../common/Comment'

class FactsShow extends React.Component {
  constructor() {
    super()

    this.state = { fact: null, comment: null}
    this.handleCommentChange = this.handleCommentChange.bind(this)
    this.handleCommentSubmit = this.handleCommentSubmit.bind(this)
    this.handleCommentDelete = this.handleCommentDelete.bind(this)
    this.handleDelete = this.handleDelete.bind(this)
    this.isOwner = this.isOwner.bind(this)
  }

  componentDidMount() {
    this.getFacts()
  }

  getFacts() {
    axios.get(`/api/facts/${this.props.match.params.id}`)
      .then(res => this.setState({ fact: res.data, comment: ''}))
      .catch(err => console.log(err))
  }

  handleDelete() {
    axios.delete(`/api/facts/${this.props.match.params.id}`, {
      headers: { Authorization: `Bearer ${Auth.getToken()}`}
    })
      .then(() => this.props.history.push('/'))
      .catch(err => console.log(err.response))
  }

  handleCommentChange({ target: { value } }) {
    const comment = value
    this.setState({ comment })
  }

  handleCommentSubmit(e){
    e.preventDefault()
    const comment = { content: this.state.comment }
    axios.post(`/api/facts/${this.props.match.params.id}/comments`, comment, {
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
      .then(() => this.getFacts())
      .catch(err => console.log(err.response))
  }

  handleCommentDelete(id) {
    axios.delete(`/api/facts/${this.props.match.params.id}/comments/${id}`, {
      headers: { 'Authorization': `${Auth.getToken()}` }
    })
      .then(() => this.getFacts())
      .catch(err => console.log(err))
  }

  isCommentOwner(user) {
    return Auth.getPayload().sub === user.id
  }

  isOwner() {
    return Auth.getPayload().sub === this.state.fact.creator.id
  }

  render() {
    if (!this.state.fact) return null
    const { fact } =  this.state
    console.log('state', this.state)
    return (
      <div className="card">
        <div className="card-header">
          <div className="card-title h4">{fact.name}</div>
          <div className="card-subtitle h5">{fact.date_of_fact} {fact.location}</div>
        </div>
        <div className="card-body">
        </div>
        <div className="card-footer">
          <div className="card-title h7">{fact.bio}</div>
        </div>
        <div className="card-image">
          <img src={fact.image} alt={fact.name}  />
        </div>
        <span>
          {this.isOwner() && <button onClick={this.handleDelete} className="btn">Delete</button>}
          {this.isOwner() && <button><Link className="button" to={`/facts/${fact.id}/edit`}
          >
        Edit
          </Link></button>}
        </span>
        {fact.comments.map(comment => console.log('comment', comment))}
        {fact.comments.map(comment => (
          <Comment
            key={comment.id}
            handleCommentDelete={this.handleCommentDelete}
            isCommentOwner={this.isCommentOwner}
            {...comment}
          />)
        )}
        {Auth.isAuthenticated() &&
          <CommentForm
            content={this.state.comment}
            handleCommentChange={this.handleCommentChange}
            handleCommentSubmit={this.handleCommentSubmit}
          />
        }
      </div>
    )
  }


}

export default FactsShow
