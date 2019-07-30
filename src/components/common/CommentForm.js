import React from 'react'

const CommentForm = ({ content, handleCommentChange, handleCommentSubmit }) => (
  <form onSubmit={handleCommentSubmit}>

    <div className="form-group">
      <textarea className="form-input"
        placeholder="Leave a Comment..."
        rows="1"
        onChange={handleCommentChange}
        name="content"
        value={content || ''}>
      </textarea>
    </div>
    <button className="btn btn-sm btn-link" type="submit">Post Comment</button>
  </form>
)

export default CommentForm
